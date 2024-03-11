class Graph:
    def __init__(self, nodes = []):
        self.nodes = nodes
    

class Node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children