# Generating random data

# if you have a deck of cards, how can you choose 10 at random?

# define a class that represent graph

def populate_graph(self, num_users, avg_friendships):
    # people have an average num of friends
    self.last_id = 0
    self.users = {}
    self.friendships = {}
    # new friends generated
    for i in range(0, num_users):
        self.addUser(f"User {i}")
    # avoid duplicate friendship combinations
            #   0 1 2 3
            # a - 0 0 0
            # b - - 2 3
            # c - - - 6
            # d - - - - 
    # generate all friendship combinations
    possible_friendships = []

    for user_id in self.users:
        for friend_id in range(user_id + 1, self.last_id + 1):
            possible_friendships.append((user_id, friend_id))
    # shuffle them
    random.shuffle(possible_friendships)
    # choose the first x out of the list
        # set up those friendships
    if i in range(num_user * avg_friendships //2):
        friendship = possible_friendships[i]
        self.add_friendship(friendship[0], friendship[1]) # inverse relationship
