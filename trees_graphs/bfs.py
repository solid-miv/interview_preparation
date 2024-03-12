import queue
import copy
from typing import Callable, List, Any


def breadth_first_search(start: Any, is_goal: Callable, next_states: List):
    """
    Implements breadth first search algorithm.

    Args:
        start: The starting state (the type is defined by the user).
        is_goal: A function that returns True if the state is the goal state.
        next_states: A function that returns a list of the next possible states.
    
    Returns:
        list: A list of states representing the path to the goal state, an empty list if no path is found.
    """
    to_do = queue.Queue()  # this queue stores the lists of states
    to_do.put([start])  # states are represented with tuples
    previously_explored = set()  # previously explored states are stored here

    while not to_do.empty():
        path = to_do.get()
        current = path[-1]

        if is_goal(current): return path  # check for the goal state

        for state in next_states(current):
            if state not in previously_explored:
                path_temp = copy.deepcopy(path)  # .copy() is used because list is a mutable object
                path_temp.append(state)
                to_do.put(path_temp)
                previously_explored.add(state)

    return []