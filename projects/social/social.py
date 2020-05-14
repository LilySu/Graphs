import sys
sys.path.append("../graph")
from graph import Graph
import random 


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def get_neighbors(self, user_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if user_id in self.friendships:
            return self.friendships[user_id]
        else:
            raise ValueError("Error: vertext does not exist")

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        self.add_friendship_counter = 0
        # !!!! IMPLEMENT ME
        # add users
        #generate all friend combinations
        # avoid duplicates by making sure num1 < num2
        
        # create friendships 

        for i in range(0, num_users):
            self.add_user(f'Fred {i+1}')
#         # avoid duplicate friendship combinations
#                 #   0 1 2 3
#                 # a - 0 0 0
#                 # b - - 2 3
#                 # c - - - 6
#                 # d - - - - 
        possible_friends=[]
        for user_id in self.users:
            for friend_id in range(user_id +1 , self.last_id +1):
                 possible_friends.append((user_id, friend_id))
        # shuffle the list and get N from the list 


        random.shuffle(possible_friends)
        # create for X pairs (tatal // 2)
        for i in range(num_users*avg_friendships //2):
            friendship =possible_friends[i]
            self.add_friendship_counter += 1
            self.add_friendship(friendship[0], friendship[1])   \

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        queue = Queue()
        queue.enqueue([user_id])
        visited = {}
        while queue.size() > 0:
        #     Dequeue the first vert
            path = queue.dequeue()
    
        #     If that vert isn't visited:
            if path[-1] not in visited:
        #         Mark as visited
        # last index is destination
                visited[path[-1]] = path
                print(path)
        #         Add all its unvisited neighbors to the queue
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path) # make a copy
                    new_path.append(next_vert)
                    queue.enqueue(new_path)
        return visited
# class User:
#     def __init__(self, name):
#         self.name = name

# class SocialGraph:
#     def __init__(self):
#         self.last_id = 0
#         self.users = {}
#         self.friendships = {}

#     def add_friendship(self, user_id, friend_id):
#         """
#         Creates a bi-directional friendship
#         """
#         if user_id == friend_id:
#             print("WARNING: You cannot be friends with yourself")
#         elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
#             print("WARNING: Friendship already exists")
#         else:
#             self.friendships[user_id].add(friend_id)
#             self.friendships[friend_id].add(user_id)

#     def add_user(self, name):
#         """
#         Create a new user with a sequential integer ID
#         """
#         self.last_id += 1  # automatically increment the ID to assign the new user
#         self.users[self.last_id] = User(name)
#         self.friendships[self.last_id] = set()

#     def populate_graph(self, num_users, avg_friendships):
#         """
#         Takes a number of users and an average number of friendships
#         as arguments

#         Creates that number of users and a randomly distributed friendships
#         between those users.

#         The number of users must be greater than the average number of friendships.
#         """
#         # Reset graph
#         # people have an average num of friends
#         self.last_id = 0
#         self.users = {}
#         self.friendships = {}
#         # new friends generated
#         for i in range(0, num_users):
#             self.add_user(f"User {i+1}")
#         # avoid duplicate friendship combinations
#                 #   0 1 2 3
#                 # a - 0 0 0
#                 # b - - 2 3
#                 # c - - - 6
#                 # d - - - - 
#         # generate all friendship combinations
#         possible_friendships = []

#         for user_id in self.users:
#             for friend_id in range(user_id + 1, self.last_id + 1):
#                 possible_friendships.append((user_id, friend_id))
#         # shuffle them
#         random.shuffle(possible_friendships)
#         # choose the first x out of the list
#             # set up those friendships
#         if i in range(num_users * avg_friendships //2):
#             friendship = possible_friendships[i]
#             self.add_friendship(friendship[0], friendship[1]) # inverse relationship




if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 10)
    print(sg.friendships)
    print('friendship counter: ')
    print(sg.add_friendship_counter)

    # getting all social paths for user 1
    # The path from 1 to 8 is [1, 8]
    # The path from 1 to 2 is [1, 10, 2]


    # connections = sg.get_all_social_paths(1)
    # print(connections)

# To create 100 users with an average of 10 friends each, how many times 
# would you need to call add_friendship()? Why? 500, because 1000/2

# If you create 1000 users with an average of 5 random friends each, 
# what percentage of other users will be in a particular user's extended social network? 
# What is the average degree of separation between a user and those in his/her extended network?