def dft_recursive(self, start_vert, visited=None):
# *explore*:
#     print this node
#     *explore* all unvisited neighbors
#     return
    print(start_vert)
    if visited is None:
        visited = set()
    
    visited.add(start_vert)

    for child_vert in self.vertices[start_vert]:
        if child_vert not in visied:
            # child becomes next starting vert for recursion
            dft_recursive(child_vert, visited)

g = Graph()
g.bft_recursive(99)


