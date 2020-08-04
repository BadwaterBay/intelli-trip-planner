#!/usr/bin/env python

"""
Solve for the fastest route
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# pylint: disable=wrong-import-position
import asyncio
from typing import Tuple
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from core.helpers.helper import seconds_in_x_hours
from core.helpers.read_write import load_dm_pickle

# pylint: disable=bad-continuation
async def create_data_model(
    distance_matrix: Tuple[Tuple[int]], duration_matrix: Tuple[Tuple[int]]
) -> dict:
    # pylint: enable=bad-continuation
    """
    # Stores the data for the route optimization problem
    """
    data = {
        "distance_matrix": distance_matrix,
        "duration_matrix": duration_matrix,
        "num_vehicles": 1,
        "depot": 0,
    }
    return data


async def get_solution(manager, routing, solution) -> dict:
    """
    # Parse solution
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


async def solve_for_plan(data: dict, measure: str, quota: int = 0) -> dict:
    """
    # Entry point of the program
    ## Arguments:
    - `data` is the `data` from `create_data_model`
    - `measure` is either "distance_matrix" or "duration_matrix"
    - `quota` is the maximum distance (in meters) or duration (in seconds).
        `quota = 0` means no quota.
    """
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

    if quota != 0:
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
        # Set a large enough penalty. In the future, penalty will be a variable, as
        # it will encourage or discourage dropping nodes.
        penalty: int = int(sum(data[measure][0]))
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
        plan = await get_solution(manager, routing, solution)
        plan["quota"] = quota if quota != 0 else None
        return plan
    return None


async def print_plan(plan: dict) -> None:
    """# Prints solution in stdout"""
    if plan is None:
        print("No solution found.")
        return
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
    return


async def main() -> None:
    """
    # Driver function
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
    await print_plan(plan)

    return


if __name__ == "__main__":
    asyncio.run(main())
