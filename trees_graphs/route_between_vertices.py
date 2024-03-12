from typing import Dict, List

from bfs import breadth_first_search


def route_between_vertices(graph: Dict[str, List[str]], start: str, end: str) -> List[str]:
    """
    Given a directed graph and 2 vertices, searches for a shortes path between them.

    Args:
        graph: A dictionary where the keys are the vertices and the values are lists of vertices.
        start: The starting vertex.
        end: The ending vertex.
    
    Returns:
        list: A list of vertices representing the shortest path between start and end, empty list if no path is found.
    """
    def is_goal(current):
        return current == end
    
    def next_states(current):
        return graph[current]

    return breadth_first_search(start, is_goal, next_states)


if __name__ == "__main__":
    graph = {
        "a": ["b", "h"],
        "b": ["d"],
        "c": ["a"],
        "d": ["c", "e", "g"],
        "e": ["b", "f"],
        "f": ["g"],
        "g": ["d"],
        "h": []
    }

    answ = route_between_vertices(graph, "h", "f")
    print(answ)