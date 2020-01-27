from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random

from ast import literal_eval

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
# traversal_path = ['n', 'n']
######################################## Beginning of the Garbage##################

def traverse_all_path(graph):

    moves = []

    # Memo this ### Create a queue/stack as appropriate
    stack = Stack()
    # put starting point in that 
    stack.push(0) #player.current_room.id
    # Make a set to keep track of where weve been
    visited = set()

    #while there is stuff in the queue/stack
    while len(visited) < len(graph):
        #   "pop" the first item
        #   DO THE THINGS!
        temp = stack.head()

        visited.add(temp)

        current_room = graph[temp]

        neighbors = current_room[1]

        undiscovered = []

        # For each edge in the item add that edge the queu/stack
        for direction, neighbor in neighbors.items():
            # if not visitied
            if neighbor not in visited:
                undiscovered.append(neighbor)

        # if there is length keep pushing the next item
        #checking for the next available room to walk to
        if len(undiscovered) > 0:
            next_room = undiscovered[0]
            stack.push(next_room)
        else:
            stack.pop()
            next_room = stack.head()
        
        #create moves array to return all rooms and direction traveled.
        for direction, neighbor in neighbors.items():
            if neighbor == next_room:
                moves.append(direction)
    
    return moves
traversal_path = traverse_all_path(room_graph)
    

    # rand_direction = ['n', 's', 'e', 'w']
    # direction = random.choice(rand_direction)
    # print('current room!! ',player.current_room.id)
    # print('current exits!! ',player.current_room.get_exits())
    # print('direction player needs to travel!!',player.travel(direction), "direction: ", direction, type(direction))
    # print('current room2@!! ',player.current_room.id)

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
# print('yeet?',room_graph)

# opposites = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# class Graph():
#     def __init__(self):
#         self.vertices = {}
#         self.visited = set ()
#         self.add_vertex(player.current_room)
#         self.last = None

#     def add_vertex(self, vertex):
#         self.vertices[vertex.id] = {
#             'n': player.current_room.n_to.id if player.current_room.n_to else None,
#             's': player.current_room.s_to.id if player.current_room.s_to else None,
#             'e': player.current_room.e_to.id if player.current_room.e_to else None,
#             'w': player.current_room.w_to.id if player.current_room.w_to else None
#         }
#         for i in ['n', 's', 'e', 'w']:
#             if self.vertices[vertex.id][i] is not None:
#                 next_verticy = self.vertices[vertex.id][i]
#                 if next_verticy not in self.vertices:
#                     self.vertices[next_verticy] = {}
#                 self.vertices[next_verticy][opposites[i]] = vertex.id

#     def move(self, direction):
#         direction_check =  player.current_room.get_exits()
#         new_neighbor = random.choice(direction_check)
        
#         if len(direction_check) == 1:
#             print('yayy BFS SEARCH YOUR WAY BACK FROM HERE')
#         ### TURNNN
#         elif direction not in direction_check:
#             print('change')
#             direction = self.direction_change(direction)
#         print("newnew",direction)
#         player.travel(direction)
#         # print(self.last)
#         # print('direction',direction, self.last)
#         traversal_path.append(direction)

#         self.add_vertex(player.current_room)
#     def direction_change(self, direction):
#         direction_check =  player.current_room.get_exits()
#         print('hi', direction, 'hi', opposites[direction])
#         for x in direction_check:
#             if x != opposites[direction]:
#                 new_direction = x
#         direction = new_direction
#         print('direction',direction ,new_direction)
#         return direction

#     def get_neighbors(self, vertex):
#         # for i in ['n', 's', 'e', 'w']:
#         new_neighbors = player.current_room.get_exits()
#         new_neighbor = random.choice(new_neighbors)
#         # if player.current_room.id not in self.visited:
#         return new_neighbor
#     # TODO DFT search stuff
#     def find_wall(self, current):
#         print('once')
#         direction = self.get_neighbors(player.current_room.id)
#         self.last = direction
        
#         while player.current_room.id not in self.visited:
#             print('curr_room', player.current_room.id)
#             self.visited.add(player.current_room.id)
#             self.move(direction)
            
            # print(player.current_room.id)


        # stack = Stack()
        # stack.push([player.current_room.id])
        # cur = None    
        # while stack.size() > 0:
        #     x = self.get_neighbors(player.current_room.id)
        #     print('STACK',stack.stack)
            
        #     # print('INIT', current.id, 'REE', player.current_room.id)
        #     path = stack.pop()
        #     curr = path[-1]
        #     # print('INIT', current.id, 'REE', player.current_room.id)
        #     # print('curr', curr)
        #     if player.current_room.id not in self.visited:
        #         y = self.get_neighbors(player.current_room.id)
        #         self.move(y)
        #         # print('checkHERE',y)
        #         for next_curr in self.vertices:
        #             print('DERP',next_curr)
        #             new_path = list(path)
        #             new_path.append(next_curr)
        #             stack.push(new_path)
        #     print('REEEE',x, y, self.get_neighbors(player.current_room.id))
        




    # # print('position:', position, 'direction:', direction)
    # # print(new_graph[position][direction])
    # queue = Queue()
    # queue.enqueue([new_graph[player.current_room.id]])
    # print('qqqq', queue.queue)
    # while new_graph[position][direction] == '?':
    #     path = queue.dequeue()
    #     print('path', path)
    #     current_room = player.current_room.id
    #     print(current_room,direction)
    #     if current_room not in visited:
    #         print('maybe?')
    #     if direction not in player.current_room.get_exits():
    #         break
    #         for friend_id in self.friendships[current_friend]:
    #                 new_path = list(path)
    #                 new_path.append(friend_id)
    #                 queue.enqueue(new_path)

    #### THIS MOVES AND TRACKS ABOUT HALF.. CANT GET ALL THE BLEEPINGS NEW_GRAPH VERTICES UPDATED.
    # ## IMPORTANT NEED TO ADD THE NEW_GRAPH TO TRACK WHERE I BEEN AND UPDATE THE GRAPH

#     new_graph = {}
# for i in range(len(room_graph)):
#     new_copy = room_graph[i][1].copy()
#     if 'n' in new_copy:
#         new_copy['n'] = '?'
#     if 's' in new_copy:
#         new_copy['s'] = '?'
#     if 'e' in new_copy:
#         new_copy['e'] = '?'
#     if 'w' in new_copy:
#         new_copy['w'] = '?'
#     new_graph[i] = new_copy
# print(new_graph)


    # while new_graph[position][direction] == '?':
    #     new_position = player.current_room.id
    #     traversal_path.append(direction)
    #     player.travel(direction)
    #     # print(new_position, player.current_room.id, new_graph[new_position])
    #     if direction not in player.current_room.get_exits():
    #         new_graph[new_position][direction] = player.current_room.id
    #         print('L00k Here!',new_position, new_graph[new_position], player.current_room.id)
    #         print('change directions!!!!', player.current_room.get_exits())
    #         if len(player.current_room.get_exits()) == 1:
    #             print('do BFS to find le way home ....BREAKING')
    #             break 
    #         # TODO if all rooms adjacent are visted also bfs to new route
    #         new_direction = player.current_room.get_exits()
    #         for x in new_direction:
    #             if x != opposites[direction]:
    #                 print('cool', x)
    #                 new_direction = x
    #         direction = new_direction
    #     # print('DERPADERP',new_graph[0])      


        
    # Memo this ### Create a queue/stack as appropriate
    # put starting point in that
    #while there is stuff in the stack
        # pop the first item
    #    curr_position = position
    #     # print('pos:', new_graph[position][direction])
    #     # if not visitied
    #     if curr_position not in visited:
    #         # DO THE THINGS! -append curr_position to the list beautifully provided AND MOVE!
    #         player.travel(direction)
    #         print('yuhyeeeet',curr_position, position)
    #         #ADD to visited
    #         visited[curr_position] = position
    #         # For each edge in the item
    #         for new_pos in new_graph[position]:
    #             # add that edge the queu/stack
    #             new_path = new_graph[position]
    #             print(new_path)
    #             new_path.append(new_pos)
    #             queue.enqueue(new_path)
    # # for x in path[1:]:
    # #     traversal_path.append(x)


    
    


# TODO BFT search stuff
# def found_wall():
    # Memo this ### Create a queue/stack as appropriate
    # put starting point in that
    #Make a set to keep track of where weve been
    #while there is stuff in the stack
        # pop the first item
        # if not visitied
            # DO THE THINGS! -append curr_position to the list beautifully provided
            # For each edge in the item
                # add that edge the queu/stack

# graph = Graph()
# print('GetNeighbors check: ',graph.get_neighbors(player.current_room.id))
# print('VERTICES HERE',graph.vertices)
# print('position', player.current_room)
# graph.find_wall(player.current_room)
print('traversal path', traversal_path)
# print('visted rooms:', graph.visited)

######################################## End of the Garbage##################
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
