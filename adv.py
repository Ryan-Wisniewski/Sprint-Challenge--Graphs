from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
def traverse_all_path():
    
    rand_direction = ['n', 's', 'e', 'w']
    direction = random.choice(rand_direction)
    print('current room!! ',player.current_room.id)
    print('current exits!! ',player.current_room.get_exits())
    print('direction player needs to travel!!',player.travel(direction), "direction: ", direction, type(direction))
    print('current room2@!! ',player.current_room.id)
    ###Plan! 
    ##make the player traverse the path! ALLLLL de path
    ##while traversing the player needs to append the curr room to the traversal path.

    ##Tidbits: Prob would be easiest two do two seperate functions. that prob call back each other until full
    ## DFT until wall. if cant walk anymore. 
    ## BFS for a close unexplored path. and walk to that starting point
    ## BFS is loofing for a '?'
    ## BFS returns a list of unexplored room id's
        # convert to list
        # add to traversal path

# TODO DFT search stuff
def find_wall():
# TODO BFT search stuff
def found_wall():


traverse_all_path()
print('traversal path', traversal_path)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
