# import sys
# sys.path.insert(0, '../graph')
from util import Queue, Stack

class Queue():
    def __init__(self):
        self.queue = [] 
        # runtime complexity of adding to end of list: O(1), to front O(n), 
        # for small numbers of n simplicity, doesn't matter
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Graph:

	def __init__(self):
		self.vertices = {}

	def add_vertex(self, vertex_id):
		self.vertices[vertex_id] = set()  # set of edges

	def add_edge(self, v1, v2):
		"""Add edge from v1 to v2."""

		# If they're both in the graph
		if v1 in self.vertices and v2 in self.vertices:
			self.vertices[v1].add(v2)

		else:
			raise IndexError("Vertex does not exist in graph")

	def get_neighbors(self, vertex_id):
		return self.vertices[vertex_id]
	
	def bfs(self, starting_vertex, destination_vertex):
		"""
		Return a list containing the shortest path from
		starting_vertex to destination_vertex in
		breath-first order.
		"""
		# Create a queue
		q = Queue()
		# Enqueue A PATH TO the starting vertex
		q.enqueue([starting_vertex])
		# Create a set to store visited vertices
		visited = set()
		# While the queue is not empty...
		while q.size() > 0:
			# Dequeue the first PATH
			path = q.dequeue()
			# GRAB THE VERTEX FROM THE END OF THE PATH
			v = path[-1]
			# Check if it's been visited
			# If it hasn't been visited...
			if v not in visited:
				# Mark it as visited
				# print(path[-1])
				visited.add(v)
				# CHECK IF IT'S THE TARGET
				if v == destination_vertex:
					# IF SO, RETURN THE PATH			
					return path
				# Enqueue A PATH TO all it's neighbors
				for neighbor in self.get_neighbors(v):
					# MAKE A COPY OF THE PATH
					path_copy = path.copy()
					path_copy.append(neighbor)
					# ENQUEUE THE COPY
					q.enqueue(path_copy)

# if path longer than current longest path, make it the longest path

	# def bft(self, starting_vertex):
	# 	"""
	# 	Print each vertex in breadth-first order
	# 	beginning from starting_vertex.
	# 	"""
	# 	# Create a queue
	# 	q = Queue()
	# 	# Enqueue the starting vertex
	# 	q.enqueue([starting_vertex])
	# 	# Create a set to store visited vertices
	# 	visited = set()
	# 	# While the queue is not empty...
	# 	while q.size() > 0:
	# 		# Dequeue, pop the first vertex
	# 		path = q.dequeue()
	# 		# Check if it's been visited
	# 		# If it hasn't been visited...
	# 		if path[-1] not in visited:
	# 			# Mark it as visited
	# 			print(path[-1])
	# 			visited.add(path[-1])
	# 			# Enqueue all it's neighbors
	# 			for next_vert in self.get_neighbors(path[-1]):
	# 				new_path = list(path)
	# 				new_path.append(next_vert)
	# 				q.enqueue(new_path)

def gets_longest_list_in_list(l):
	list_len = [len(i) for i in l]
	longest = max(list_len)
	for i in range(len(list_len)):
		if len(l[i]) == longest:
			return l[i]

		# return visited

# def earliest_ancestor(ancestors, starting_node):
# 	g = Graph()
# 	g.add_vertex



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
g = Graph()
for i,j in test_ancestors:
	# insert everything into a graph
	g.add_vertex(i)
	g.add_vertex(j)
	g.add_edge(i,j)

	(g.bfs(i,j))
		# self.assertEqual(earliest_ancestor(test_ancestors, 2), -1)
		# self.assertEqual(earliest_ancestor(test_ancestors, 3), 10)
		# self.assertEqual(earliest_ancestor(test_ancestors, 4), -1)
		# self.assertEqual(earliest_ancestor(test_ancestors, 5), 4)
		# self.assertEqual(earliest_ancestor(test_ancestors, 6), 10)
		# self.assertEqual(earliest_ancestor(test_ancestors, 7), 4)
		# self.assertEqual(earliest_ancestor(test_ancestors, 8), 4)
		# self.assertEqual(earliest_ancestor(test_ancestors, 9), 4)
		# self.assertEqual(earliest_ancestor(test_ancestors, 10), -1)
		# self.assertEqual(earliest_ancestor(test_ancestors, 11), -1)


# def earliest_ancestor(ancestors, starting_node):

# 		q = Queue()
# 		q.enqueue(starting_node)

# 		# Keep track of visited nodes
# 		visited = set()

# 		# Repeat until queue is empty
# 		while q.size() > 0:
			
# 			# Dequeue first vert
# 			v = q.dequeue()

# 			# If it's not visited:
# 			if v not in visited:
# 				print(v)

# 				# Mark visited
# 				visited.add(v)

# 				for next_vert in get_neighbors(v):
# 					q.enqueue(next_vert)
	# q = Queue()
	# q.enqueue(starting_node)
	# visited = set()

	# path = []
	# # while there are no more nodes to explore 
	# # repeat until queue is empty
	# while q.size() > 0:
	#     # dequeue first vert
	#     v = q.dequeue()
	#     # if not visited
	#     if v not in visited:
	#         # mark visited 
	#         visited.add(v)
	#         path = path + [v]
	#         for next_vert in self.get_neighbors(v):
	#             q.enqueue(next_vert)
	#             if next_vert not in visited:
	#                 new_path = self.bfs_recursive(next_vert, starting_node)
	#                 if new_path:
	#                     return new_path

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# earliest_ancestor(test_ancestors, 1)
# answer is 10
