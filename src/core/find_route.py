#!/usr/bin/env python

"""
# Find the optimal routing optimal_route
"""

import sys
import os
import asyncio
from typing import Tuple, List, Union
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.helpers.general import get_seconds_in_x_hours
from core.helpers.read_write import load_pickle


async def construct_premise_for_solving_for_optimal_route(
    distance_matrix: Union[Tuple[Tuple[int]], List[List[int]]] = None,
    duration_matrix: Union[Tuple[Tuple[int]], List[List[int]]] = None,
    depot_index: int = 0,
) -> Union[dict, None]:
    if distance_matrix is None and duration_matrix is None:
        print(
            "Neither distance matrix or duration matrix were given."
            " At least one of them must be present. Return None.",
            file=sys.stderr,
        )
        return None

    return {
        "distance_matrix": distance_matrix,
        "duration_matrix": duration_matrix,
        "num_vehicles": 1,
        "depot": depot_index,
    }


async def parse_optimal_route(manager, routing, solution) -> dict:
    index = routing.Start(0)
    optimal_route = {
        "waypoints": [],
        "objective_value": solution.ObjectiveValue(),
        "true_value": 0,
    }
    while not routing.IsEnd(index):
        optimal_route["waypoints"].append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        optimal_route["true_value"] += routing.GetArcCostForVehicle(
            previous_index, index, 0
        )
    optimal_route["waypoints"].append(manager.IndexToNode(index))
    return optimal_route


async def solve_for_optimal_route(
    routing_premise: dict = None,
    measure: str = "distance_matrix",
    quota: int = 0,
    penalty: int = 0,
) -> Union[dict, None]:
    """
    # Entry point for solving for routing optimal_route
    """

    if routing_premise is None:
        print(
            "Error occurred in solve_for_optimal_route. routing_premise model is empty.",
            file=sys.stderr,
        )
        return None

    if routing_premise[measure] is None:
        print(
            "Error occurred in solve_for_optimal_route. "
            + routing_premise[measure]
            + " is None.",
            file=sys.stderr,
        )
        return None

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(
        len(routing_premise[measure]),
        routing_premise["num_vehicles"],
        routing_premise["depot"],
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
        return routing_premise[measure][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(measure_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    quota_rounded = round(quota)

    if round(quota_rounded) > 0:
        # Add distance/duration quota.
        dimension_name = measure.split("_")[0]
        routing.AddDimension(
            transit_callback_index,
            0,  # slack value
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
            penalty = int(sum(routing_premise[measure][0]))
        for node in range(1, len(routing_premise[measure])):
            routing.AddDisjunction([manager.NodeToIndex(node)], penalty)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()

    # pylint: disable=no-member
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    # pylint: enable=no-member

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        optimal_route = await parse_optimal_route(manager, routing, solution)
        optimal_route["quota"] = quota_rounded if quota_rounded > 0 else None
        return optimal_route
    return None


async def print_optimal_route(optimal_route: Union[dict, None] = None) -> bool:
    if optimal_route is None:
        print("No solution found.")
        return False
    printout: str = ""
    length: int = len(optimal_route["waypoints"])
    for i in range(length):
        if i > 0:
            printout += " "
        printout += "{}".format(optimal_route["waypoints"][i])
        if i < length - 1:
            printout += " ->"
    print("Objective: {} units".format(optimal_route["objective_value"]))
    print("True: {} units".format(optimal_route["true_value"]))
    print("Quota: {} units".format(optimal_route["quota"]))
    print(printout)
    return True


async def main() -> bool:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "data", "parsed_distance_matrix.pkl")

    distance_matrix = await load_pickle(file_path)
    routing_premise = await construct_premise_for_solving_for_optimal_route(
        distance_matrix["distance"], distance_matrix["duration"]
    )

    one_day = get_seconds_in_x_hours(8)
    optimal_route = await solve_for_optimal_route(
        routing_premise, "duration_matrix", one_day
    )
    return await print_optimal_route(optimal_route)


if __name__ == "__main__":
    asyncio.run(main())
