import queue


def deapth_first_search(state, is_goal, next_states):
    to_do = queue.LifoQueue()  # this stack stores the lists of states
    to_do.put([state])  # states are represented with tuples
    previously_explored = set()  # previously explored states are stored here

    while not to_do.empty():
        path = to_do.get()
        current = path[-1]

        if is_goal(current): return path  # check for the goal state

        for state in next_states(current):
            if state not in previously_explored:
                path_temp = path.copy()  # .copy() is used because list is a mutable object
                path_temp.append(state)
                to_do.put(path_temp)
                previously_explored.add(path_temp)

    raise ValueError("FAILURE: NO PATH FOUND")