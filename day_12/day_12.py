import os
import sys
from string import ascii_lowercase
from collections import deque


root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

ALPHA_DICT = {v: k for k, v in enumerate(ascii_lowercase)}

def data_load()->list:
	# ./day/
	with open('./day_12/test_data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [[ALPHA_DICT[x] if x.islower() else ALPHA_DICT[x.lower()] for x in list(line)] for line in data]
		start_stop = [[(data.index(line), line.index(x)) for x in list(line) if x.isupper()] for line in data]
		ss = []
		for x in start_stop:
			if len(x) > 0:
				ss.append(x)
	return arr, ss


def get_direction(direction:str)->tuple:
	DIRECTIONS = {
		"U":(0, -1),
		"D":(0,  1), 
		"L":(-1, 0),
		"R":(1,  0)
	}
	return DIRECTIONS[direction]

def on_board(data:list, x1:int, y1:int)->bool:
	wd = len(data[0])
	ht = len(data)
	# ht = data.shape[1]

	if x1 < 0 or y1 < 0 or x1 >= ht or y1 >= wd:
		return False
	else:
		return True


def calc_part_A(grid:list, start_stop:list)->int:
	#grid layout
	# # # # # # # 
	#x---------->
	#y#
	#|#
	#|#
	#|#
	#v# # # # # #
	start = start_stop[0][0]
	end = start_stop[1][0]
	steps = 0
	dirs = ['U','D','L','R']
	step_list = []
	visited = set()

	while start != end:
		#Dangerous using that as it could get lost. 
		for direction in dirs:
			step = get_direction(direction)
			next_loc = (start[0] + step[0], start[1] + step[1])
			if on_board(grid, next_loc[0], next_loc[1]):
				mount_diff = grid[start[0] + step[0]][start[1] + step[1]] - grid[start[0]][start[1]]
				step_list.append((next_loc, mount_diff, direction))

		#Fix this
		step_list = sorted(step_list, key = lambda x: x[1], reverse=True)
		for loc in step_list:
			if step_list[0][1] > 1:
				step_list.pop(0)
				continue	

			if loc[0][1] <= 1:
				if loc not in visited:
					visited.add(loc[0])
					# dx, dy = step_list[0][0][0], step_list[0][0][1]
					start = loc[0]
					break

		#reset best_step to zero and increase
		step_list = []
		steps += 1		
	return steps
	
		


	#req's
	#Can only move up down left right
	#elevation of movement MUST be no more than 1 higher than current pos
	#elevation can be lower though

	#First check is to see if move is on board.
	#Second check is to see if dir is 1 step higher
	#third check is to see if any are lower. 

@log_time
def run_part_A():
	data, start_stop = data_load()
	step_count = calc_part_A(data, start_stop)
	return step_count

@log_time
def run_part_B():
	data = data_load()
	
print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")


#NOTE - So it look slike i'd need to do a bfs tree search on this to find the shortest
#path.  But i don't feel like doing that because tree algorithms are annoying to implement
#So skipping day12 and goign to 13

