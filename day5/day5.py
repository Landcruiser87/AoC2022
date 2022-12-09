# AOC Day 5 - Supply Stacks

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
	#Make a dict of the string index of each cargo numbers label.
	# key = label of container (the enumerate should correspond to the label)
	# val = string position of the the label (ie-the letter position) 
	cargo_pos_dict = {int(v):k for k, v in enumerate(cargo_map_str) if v.isdigit()}
	#Make a dict of lists to hold the cargo manifest
	cargo_dict = {k:[] for k in cargo_pos_dict.keys()}

	#Loop through the maps and add each cargo to its correct bin. 
		#NOTE: Uses the cargo_pos_dict to look up each letter in the string.
	for row in range(len(cargo_map)):
		for key, val in cargo_pos_dict.items():
			if cargo_map[row][val].isalpha():
				cargo_dict[key] += cargo_map[row][val]

	#Loop through and pull out the numeric instructions of the input.
	#make each instruction into a list of ints.
	for move in range(len(moves)):
		mov_str = moves[move].split(" ")
		moves[move] = [int(x) for x in mov_str if x.isdigit()]

	#!remember.  TOP items are at the start of the lists
	return cargo_dict, moves
	
def calc_topcrates(cargo_dict:dict, moves:list, part:str):
	#Notes
	#moves[0] = num of cargo to move
	#moves[1] = where to move it from
	#moves[2] = where to move it too

	for move in moves:
		if part == 'part_A':
			while move[0] > 0:
				cargo_dict[move[2]].insert(0, cargo_dict[move[1]].pop(0))
				move[0] -= 1

		if part == 'part_B':
			containers = cargo_dict[move[1]][:move[0]]
			del cargo_dict[move[1]][:move[0]]
			[cargo_dict[move[2]].insert(0, x) for x in containers[::-1]]
				
	top_crates = "".join(cargo_dict[key][0] for key in cargo_dict.keys())
	return top_crates

@log_time
def run_part_A():
	cargo_map, moves = data_load()
	top_crates = calc_topcrates(cargo_map, moves, 'part_A')
	return top_crates

@log_time
def run_part_B():
	cargo_map, moves = data_load()
	top_crates = calc_topcrates(cargo_map, moves, 'part_B')
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

