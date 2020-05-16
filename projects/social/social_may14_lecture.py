def populate_graph_linear(self, num_users, avg_friendships):
    self.last_id = 0
    self.users = {}
    self.friendships = {}

    # first 2 is o, but after awhile it will take a long time to hit those friends
    # add users

    for i in range(num_users):
        self.addUser(f"User {i+1}")
    target_friendships = num_users *
    total_friendships = 0
    collisions = 0 

    while total_friendships < target_friendships:
        user_id = random.randint(1, self.last_id)
        friend_id = random.randint(1, self.last_id)

        # this part slows it down an array can be created that is scrambled
        if self.add_friendship(user_id, friend_id):
            total_friendships += 2
        else:
            collisions += 1