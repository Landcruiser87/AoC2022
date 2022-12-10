# AOC Day 9 - Rope Bridge
import os
import sys
from collections import deque


root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

def data_load()->list:
	# ./day/
	with open('./day9/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [x.split() for x in data]
	return arr

def move_knot(move:str)->tuple([int, int]):
	direction_dict = {
		"U":(0, 1),
		"D":(0, -1), 
		"L":(-1, 0),
		"R":(1, 0)
	}

	return direction_dict[move]

def tail_check(head:tuple, tail:tuple)->tuple:
	#Find the difference in the head and tail. Move the tail position by the
	#delta // abs(delta) to get a single step movevment
	dx, dy = (head[0]-tail[0], head[1]-tail[1])
	#1.  If both dx, dy abs difference is less than 1
		#return the tail as is.  Doesn't need adjustment
	if abs(dx) <= 1 and abs(dy) <=1:
		return (tail[0], tail[1])

	#2.  if deltax > 1 - Move in X direction
	elif abs(dx) > 1 and abs(dy) == 0:
		return (tail[0] + dx // abs(dx), tail[1])

	#3. if deltay > 1 - Move in Y direction
	elif abs(dy) > 1 and abs(dx) == 0:
		return (tail[0], tail[1] + dy // abs(dy))

	#4. if deltax and deltay > 1.  Move in diag
	elif abs(dx) > 0 and abs(dy) > 0:
		return (tail[0] + dx // abs(dx) , tail[1] + dy // abs(dy))

	#5. All other cases, return zero tuple
	else:
		return (0, 0)
	

def calc_part_A(moves:list):
	#grid layout
	#^#
	#|#
	#|#
	#|#
	#y# # # # # #
	#x---------->
	# # # # # # # 

	h_moves = deque(moves)
	head = tail = (0, 0)
	tail_seen = set([tail])

	while h_moves:
		move, move_count = h_moves.popleft()
		steps = int(move_count)
		while steps > 0:
			x_move, y_move = move_knot(move)
			head = (head[0] + x_move, head[1] + y_move)
			tail = tail_check(head, tail)
			tail_seen.add(tail)
			steps -= 1

	return len(tail_seen)

	#Part A Gameplan
	#I'll need a function to check the tail at EVERY step
	#1. Move the head knot in a desired direction
		#Use a dict of movemvents in each direction
	#2. Have a tail check function that returns 
		#wether its "kissing" aka touching the current head value. 
		#-If it does, do nothing
		#-If it doesn't, move the tail and
		#add it to the tail_seen set

def calc_part_B(moves):
	#grid layout
	#^#
	#|#
	#|#
	#|#
	#y# # # # # #
	#x---------->
	# # # # # # # 

	h_moves = deque(moves)
	tail = (0, 0)
	tail_seen = set([tail])
	knot_list = [(0,0) for _ in range(10)]

	while h_moves:
		move, move_count = h_moves.popleft()
		steps = int(move_count)
		while steps > 0:
			x_move, y_move = move_knot(move)
			knot_list[0] = (knot_list[0][0] + x_move, knot_list[0][1] + y_move)
			for knot_idx in range(1, len(knot_list)):
				knot_list[knot_idx] = tail_check(knot_list[knot_idx-1], knot_list[knot_idx])
			tail_seen.add(knot_list[-1])
			steps -= 1

	return len(tail_seen)

@log_time
def run_part_A():
	data = data_load()
	num_visits = calc_part_A(data)
	return num_visits

@log_time
def run_part_B():
	data = data_load()
	num_visits = calc_part_B(data)
	return num_visits
	
print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")

#Notes
#Part A

#What a weird problem.  
#Ok.  so we've got a rope bridge that has directional inputs
#on a 2d grid. (think giant game of snake)

#A rope has 1
#T = Tail
#H = Head

#Our task is to move the head around the grid and track the tail position while
#adhering to the following rules

#1. The rope is short
#2. T and H must ALWAYS be touching
	#Diag, L, R, U, D.  AND overlap.
	#Does it exist in a grid around the updated head point
#3. Head and tail start at the same position. (Overlapping)

#4. If head is ever two steps directly up/down/L/R of tail. 
	#tail must also move one step in that direction to keep up

#4. If Head moves so that
	# They're not touching 
	# or
	# out of row/col of tail.
		#-Tail moves diagonally to catch up