# search unvisited land spots
# increment counter for each island we traverse
# ignore explored land
# traverse entire island
# mark visited
# use a stack
# push neighbors on stack
# instead of having an adjacency matrix or list, we had an unwritten rule that if 1 is adjacent to another, they were connected
# for getting neighbors, we looked to north by subtracting current row ie. 

islands = [[1,1,0,0,1],
            [1,0,0,0,1],
            [0,0,1,0,0],
            [1,0,1,0,1],
            [1,1,0,1,1]]

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# depth first with cycles or directional will not get you shortest path

def island_counter(matrix):
    # Create a visited data structure
    visited = []

    for i in range(len(matrix)):
        # Every cell has False instead
        visited.append([False] * len(matrix[0])) # append me a list of the width of the input

    island_count = 0
    # walk through all nodes, elements in the input matrix
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
    # if it is not visited
            if not visited[row][col]:
    # if the value in teh matrix at this posiition is 1:
                if matrix[row][col] == 1:
    # do a traversal and mark each as visited
    # start from whatever row and column we're at and do traversal
                    visited = dft(row, col, matrix, visited)
    # increment island counter
                    island_count += 1
                else:
                    # we hit 0, or water, mark as visited
                    visited[row][col] = True
    return island_count

def dft(row, col, matrix, visited):
    s = Stack()
    # push starting vert on the stack
    # we use a tuple to identify a vertex
    s.push((row, col))

    while s.size() > 0:
        # pop first vert
        v = s.pop()
        row, col = v
        # if not visited, traverse
        if not visited[row][col]:
            # mark visited
            visited[row][col]= True
            # push neighbors on stack
            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)

    return visited

def get_neighbors(row, col, matrix):
    neighbors = []

    # check north
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.append((row-1, col))
    # check south
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        neighbors.append((row+1, col))
    # check west
    if col > 0 and matrix[row][col - 1] == 1:
        neighbors.append((row, col - 1))
    # check east
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] == 1:
        neighbors.append((row, col+1))

    return neighbors

print(island_counter(islands))