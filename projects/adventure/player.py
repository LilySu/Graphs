

class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")

# Start by writing an algorithm that picks a random unexplored direction 
# from the player's current room, travels and logs that direction, 
# then loops. This should cause your player to walk a depth-first traversal. 
# When you reach a dead-end (i.e. a room with no unexplored paths), 
# walk back to the nearest room that does contain an unexplored path.

# You can find the path to the shortest unexplored room by using a 
# breadth-first search for a room with a `'?'` for an exit. 
# If you use the `bfs` code from the homework, you will need to make a 
# few modifications.

# 1. Instead of searching for a target vertex, you are searching for 
# an exit with a `'?'` as the value. If an exit has been explored, 
# you can put it in your BFS queue like normal.

# 2. BFS will return the path as a list of room IDs. You will need 
# to convert this to a list of n/s/e/w directions before you can 
# add it to your traversal path.

# If all paths have been explored, you're done!


# just make the player traverse the entire thing
# traversal comment out and put in your own repl

# figure out how are you going to traverse it - bft, dft - bft best
