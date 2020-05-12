class Graph:
    def __init__(self):
        self.vertices = {}  # adjacency list

    def add_vertex(self, vertex_id):
        # we use set because we only have 1 connection to each edge
        # lookup (O)1
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # check if they exist
        if v1 in self.vertices and v2 in self.vertices: # directed
            # add edge
            self.vertices[v1].add(v2)

        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id): 
        # return a set of all the edges a vertex has 
        # check it 
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:

        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):

        q = Queue()
        q.enqueue(starting_vertex_id)

        # keep track of visited nodes
        visited = set()

        while q.size() > 0:

            # dequeue first vert
            v = q.dequeue()

            # If it's not visited:
            if v not in visited: # order 1 lookup check to see in there
                visited.add(v)

                for next_vert in self.get_neighbors(v):

g = Graph()
g.add_vertex(99)
g.add_vertex(3)
g.add_edge(99, 3)
g.add_edge(99,3490)
g.add_edge(3,99)

print(g.get_neighbors(99))
print(g.get_neighbors(3))
    