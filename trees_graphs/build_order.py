from collections import defaultdict
import queue

# O(P + D); P - number of projects, D - number of dependencies
def build_order(projects, dependencies):
    graph = defaultdict(list)
    incoming_degree = defaultdict(int)

    for dependency in dependencies:
        dependency_project, main_project = dependency
        graph[dependency_project].append(main_project)
        incoming_degree[main_project] += 1

    build_order = []

    # store the projects with no dependencies in no_dependencies_queue
    no_dependencies_queue = queue.Queue()
    for project in projects:
        if incoming_degree[project] == 0:
            no_dependencies_queue.put(project)

    while not no_dependencies_queue.empty():
        project = no_dependencies_queue.get()
        build_order.append(project)

        for dependent in graph[project]:
            incoming_degree[dependent] -= 1

            if incoming_degree[dependent] == 0:
                no_dependencies_queue.put(dependent)

    if len(build_order) != len(projects):
        raise ValueError("No valid build order exists")

    return build_order


if __name__ == '__main__':
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

    # projects = ['a', 'b', 'c'] 
    # dependencies = [('a', 'b'), ('b', 'c'), ('c', 'a')]  # cycle
    
    order = build_order(projects, dependencies)
    print(order)