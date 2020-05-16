from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
# traversal_path_dict = ['n', 'n']
traversal_path_dict = []

# because player moves in both drections n-s e-w  and room has two exits!
reversed_path_dict = []

# You may find the commands `player.current_room.id`, - gettting ids of every room
# `player.current_room.get_exits()` - gets all possible exits
# and `player.travel(direction)` useful. - travels in that direction 


path_dict = {} # rooms 
path_dict[0] = player.current_room.get_exits()
visitedRoute = []

reverse = { 'e': 'w' ,'w' :'e','n' :'s', 's': 'n',}

while len(path_dict) < len(room_graph) -1:

    if player.current_room.id not in path_dict:
        path_dict[player.current_room.id] = player.current_room.get_exits()
        previous_room = reversed_path_dict[-1]
        path_dict[player.current_room.id].remove(previous_room)

    while len(path_dict[player.current_room.id]) < 1:
        visited = reversed_path_dict.pop()
        traversal_path_dict.append(visited)
        player.travel(visited)
    exits = path_dict[player.current_room.id].pop()
    traversal_path_dict.append(exits)
    reversed_path_dict.append(reverse[exits])
    player.travel(exits)

if len(traversal_path_dict)<2000:
    for i in traversal_path_dict:
        print(f"walk {i} to get to next room") 

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path_dict:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path_dict)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
