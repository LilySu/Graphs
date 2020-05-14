# bfs is guaranteed to get shortest path

# bft is needed for the social networks because bfs might miss possible shortest solutions 
# because bfs might stop at the solution
def bfs(self, starting_vertex)
    while q.size() > 0:
        path = d.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if v == destination_vertex:
                return path
            for next_vert in self.get_neighbors(v):
                new_path = path.copy()
                new_path.append(next_vert)
                q.enqueue(new_path) # pass in new_path into queue
    