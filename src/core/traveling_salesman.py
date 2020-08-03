#!/usr/bin/env python

"""
Solve for the fastest route
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# pylint: disable=wrong-import-position
import asyncio
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from core.helpers.read_write import load_dm_pickle


async def create_data_model(distance_matrix):
    """Stores the data for the problem."""
    data = {"distance_matrix": distance_matrix, "num_vehicles": 1, "depot": 0}
    return data


async def get_solution(manager, routing, solution):
    """Prints solution on console."""
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


async def solve_for_plan(data):
    """Entry point of the program."""

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(
        len(data["distance_matrix"]), data["num_vehicles"], data["depot"]
    )

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    # pylint: disable=no-member
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    # pylint: enable=no-member

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        plan = await get_solution(manager, routing, solution)
        return plan


async def print_plan(plan) -> None:
    """Prints solution in stdout"""
    if plan is None:
        print("No solution found.")
        return
    plan_output = ""
    length = len(plan["waypoints"])
    for i in range(length):
        if i > 0:
            plan_output += " "
        plan_output += "{}".format(plan["waypoints"][i])
        if i < length - 1:
            plan_output += " ->"
    print("Objective: {} meters".format(plan["objective_value"]))
    print("True: {} meters".format(plan["true_value"]))
    print(plan_output)
    return


async def main():
    """
    Driver function
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "data", "parsed_distance_matrix.pkl")

    # Instantiate the data problem.
    distance_matrix = await load_dm_pickle(file_path)
    data = await create_data_model(distance_matrix["distance"])

    plan = await solve_for_plan(data)
    await print_plan(plan)


if __name__ == "__main__":
    asyncio.run(main())
