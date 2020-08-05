#!/usr/bin/env python

"""
Solve for the fastest route
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# pylint: disable=wrong-import-position
import asyncio
from typing import Tuple, List, Union
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from core.helpers.helper import seconds_in_x_hours
from core.helpers.read_write import load_dm_pickle


# pylint: disable=bad-continuation
async def create_data_model(
    distance_matrix: Union[Tuple[Tuple[int]], List[List[int]]] = None,
    duration_matrix: Union[Tuple[Tuple[int]], List[List[int]]] = None,
    depot_index: int = 0,
) -> Union[dict, None]:
    """
    # Stores the data for the route optimization problem
    - :param distance_matrix: 2D tuple or list of a distance matrix.
    - :param duration_matrix: 2D tuple or list of a duration matrix.
    - :param depot_index: The index of depot (that is, the origin and the
    final destination) in the matrix. It should be a single integer, as the
    matrix is symmetrical.
    - :type distance_matrix: Tuple[Tuple[int]] | List[List[int]]
    - :type duration_matrix: Tuple[Tuple[int]] | List[List[int]]
    - :type depot_index: int
    - :return: Data model for OR-Tool.
    - :rtype: dict | None
    """
    if distance_matrix is None and duration_matrix is None:
        print(
            "Neither distance matrix or duration matrix were given."
            "At least one of them must be present. Return None.",
            file=sys.stderr,
        )
        return None

    return {
        "distance_matrix": distance_matrix,
        "duration_matrix": duration_matrix,
        "num_vehicles": 1,
        "depot": depot_index,
    }


async def parse_plan(manager, routing, solution) -> dict:
    """
    # Parse routing plan
    :return: Routing plan
    :rtype: dict
    """
    index = routing.Start(0)
    plan = {
        "waypoints": [],
        "objective_value": solution.ObjectiveValue(),
        "true_value": 0,
    }
    while not routing.IsEnd(index):
        plan["waypoints"].append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        plan["true_value"] += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan["waypoints"].append(manager.IndexToNode(index))
    return plan


async def solve_for_plan(
    data: dict = None,
    measure: str = "distance_matrix",
    quota: int = 0,
    penalty: int = 0,
) -> Union[dict, None]:
    """
    # Entry point for solving for routing plan
    - :param data: the `data` from `create_data_model`.
    - :param measure: "distance_matrix" (default) and "duration_matrix".
    - :param quota: Nonnegative integer representing the maximum distance (in
    meters) or duration (in seconds). `quota = 0` means no quota.
    - :param penalty: Penalty for dropping destinations.
    - :type data: dict
    - :type measure: str
    - :type quota: int
    - :type penalty: int
    - :return: The routing plan.
    - :rtype: dict | None
    """

    if data is None:
        print("Error occurred in solve_for_plan. Data model is empty.", file=sys.stderr)
        return None

    if data[measure] is None:
        print(
            "Error occurred in solve_for_plan. " + data[measure] + " is None.",
            file=sys.stderr,
        )
        return None

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(
        len(data[measure]), data["num_vehicles"], data["depot"]
    )

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    def measure_callback(from_index, to_index):
        """
        # Returns the distance or duration between the two nodes
        """
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data[measure][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(measure_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    quota_rounded = round(quota)

    if round(quota_rounded) > 0:
        # Add distance/duration quota.
        dimension_name = measure.split("_")[0]
        routing.AddDimension(
            transit_callback_index,
            0,  # no slack
            quota,  # vehicle maximum travel distance/duration
            True,  # start cumul to zero
            dimension_name,
        )
        distance_dimension = routing.GetDimensionOrDie(dimension_name)
        distance_dimension.SetGlobalSpanCostCoefficient(0)

        # Allow to drop nodes.
        # Set a large enough penalty. In the future, penalty will be a variable,
        # as it will encourage or discourage dropping nodes.
        if isinstance(penalty, int) or penalty <= 0:
            penalty = int(sum(data[measure][0]))
        for node in range(1, len(data[measure])):
            routing.AddDisjunction([manager.NodeToIndex(node)], penalty)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()

    # pylint: disable=no-member
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    # pylint: enable=no-member

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Return solution
    if solution:
        plan = await parse_plan(manager, routing, solution)
        plan["quota"] = quota_rounded if quota_rounded > 0 else None
        return plan
    return None


async def print_plan(plan: Union[dict, None] = None) -> bool:
    """
    # Prints solution in stdout
    - :param plan: Routing plan
    - :type plan: dict | None
    - :return: Boolean
    - :rtype: bool
    """
    if plan is None:
        print("No solution found.")
        return False
    plan_output: str = ""
    length: int = len(plan["waypoints"])
    for i in range(length):
        if i > 0:
            plan_output += " "
        plan_output += "{}".format(plan["waypoints"][i])
        if i < length - 1:
            plan_output += " ->"
    print("Objective: {} units".format(plan["objective_value"]))
    print("True: {} units".format(plan["true_value"]))
    print("Quota: {} units".format(plan["quota"]))
    print(plan_output)
    return True


async def main() -> bool:
    """
    # Driver function for development purposes
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "data", "parsed_distance_matrix.pkl")

    # Instantiate the data problem.
    distance_matrix = await load_dm_pickle(file_path)
    data = await create_data_model(
        distance_matrix["distance"], distance_matrix["duration"]
    )

    one_day = seconds_in_x_hours(8)  # An 8-hour day
    plan = await solve_for_plan(data, "duration_matrix", one_day)
    return await print_plan(plan)


if __name__ == "__main__":
    asyncio.run(main())
