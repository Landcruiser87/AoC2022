import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

def data_load()->list:
	# ./day5/
	with open('./day5/data.txt', 'r') as f:
		data = f.read().splitlines()
		cargo_map, moves = data[:data.index('')], data[data.index('')+1:]

	cargo_map_str = cargo_map.pop()
	#Make a dict of the index of each cargo letter. 
	cargo_pos_dict = {int(v):k for k, v in enumerate(cargo_map_str) if v.isdigit()}
	#Make a dict of lists for containers. 
	cargo_dict = {k:[] for k in cargo_pos_dict.keys()}

	for row in range(len(cargo_map)):
		for key, val in cargo_pos_dict.items():
			if cargo_map[row][val].isalpha():
				cargo_dict[key] += cargo_map[row][val]

	for move in range(len(moves)):
		mov_str = moves[move].split(" ")
		moves[move] = [int(x) for x in mov_str if x.isdigit()]

	#!remember.  TOP items are at the start of the lists
	return cargo_dict, moves
	
def calc_part_A(cargo_dict, moves):
	#Notes
	#cargo map = zero indexed list of containers. 
	#moves[0] = num of cargo to move
	#moves[1] = where to move it from
	#moves[2] = where to move it too

	for move in moves:
		while move[0] > 0:
			cargo_dict[move[2]].insert(0, cargo_dict[move[1]].pop(0))
			move[0] -= 1

	top_crates = "".join(cargo_dict[key][0] for key in cargo_dict.keys())
	
	return top_crates

def calc_part_B(cargo_dict, moves):
	#Notes
	#Now our crane can grab multiple crates at once....
		#So we'll need to change the iteration.  
		#Take out while loop

	#cargo map = zero indexed list of containers. 
	#moves[0] = num of cargo to move
	#moves[1] = where to move it from
	#moves[2] = where to move it too

	for move in moves:
		containers = cargo_dict[move[1]][:move[0]]
		del cargo_dict[move[1]][:move[0]]
		[cargo_dict[move[2]].insert(0, x) for x in containers[::-1]]


	top_crates = "".join(cargo_dict[key][0] for key in cargo_dict.keys())
	
	return top_crates


@log_time
def run_part_A():
	cargo_map, moves = data_load()
	top_crates = calc_part_A(cargo_map, moves)
	return top_crates

@log_time
def run_part_B():
	cargo_map, moves = data_load()
	top_crates = calc_part_B(cargo_map, moves)
	return top_crates
	

print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")

#Notes
	#What a b of a puzzle input. 
#GOAL
	#The elves have stacks of crates that need to be moved by a crane operator.
	#We know where each container starts, and the moves of each stack to get to
	#the final position. 

#Part A
	#Our job is to figure out what crate is on top of each stack. 
		#need to be a string of letters in return. 

#Part B
	#Now our crane operator can move multiple crates at once.  
	#soooooo  now we need to index all the crates movements in the order they
	#are selected

