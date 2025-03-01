class Vertex:
    def __init__(self, val):
        self.val = val
        self.neighbours = {}

    def add_to_neighbours(self, neighbour, w):
        self.neighbours[neighbour] = w

    def get_neighbours(self):
        return self.neighbours.keys()
    

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, val):
        new_vertex = Vertex(val)
        self.vertices[val] = new_vertex
        return new_vertex
    
    def add_edge(self, u, v, weight):
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)
        self.vertices[u].add_to_neighbours(v, weight)
    
    def get_vertex(self, val):
        return self.vertices[val]
    
    def get_vertices(self):
        return self.vertices.keys()
    
    def __iter__(self):
        return iter(self.vertices)
    
