class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = [] # Adjacency List


# Breadth-First Traversal
# Add starting node to a queue
# While queue isn't empty:
#     Dequeue the first vert
#     If that vert isn't visited:
#         Mark as visited
#         Add all its unvisited neighbors to the queue

# Depth-First Traversal
# Add starting node to a stack
# While stack isn't empty:
#     Pop the first vert
#     If that vert isn't visited:
#         Mark as visited
#         Push all its unvisited neighbors to the stack

# depth first - uses a stack, call stack can use recursion, 
# - last in first out
# backtracking exhaustive search 
# explores everything


# breath first - uses a queue first in first out
# if there is a path between two nodes
# going wide, slowing increasing the distance from start node

