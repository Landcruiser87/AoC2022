# AOC Day 8 - Treetop Tree House

import numpy as np
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

def data_load()->list:
	# ./day8/
	with open('./day8/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = np.array([[int(x) for x in list(line)] for line in data], dtype='int')
	return arr

def tree_is_visible(grid:list, x:int, y:int)->bool:
	#eval the visibility in each direction from the location of the tree. So
	#we'll need to iterate through each tree's location and then look out each
	#direction if we have a clear view, tree is visible and exit loop

	# Gameplan 
	#1. Outer tree's are all visible.  So immediately increase the count by the shape of the array. 
	#2. For a tree to qualify as visible.  It has to be viewable from at least 1 side of the grid. 
		#Could have just checked with all().  oh well. 
	
	#grid layout
	#y---------->
	
	#x
	#|
	#|
	#|
	#v

	directions = {
		'N': grid[:x, y],
		'S': grid[x+1:, y],
		'E': grid[x, y+1:],
		'W': grid[x, :y],
	}
	#Loop through the directions values
	#Check that max value in the vector is less than the grid value
	for coords in directions.values():
		if max(coords) < grid[x,y]:
			return True

	return False

def calc_tree_score(grid:list, x:int, y:int)->int:
	#Now we need to calculate the score of each view in each direction. 
	#grid layout
	#y---------->
	
	#x
	#|
	#|
	#|
	#v

	directions = {
		'N': grid[:x, y],
		'S': grid[x+1:, y],
		'E': grid[x, y+1:],
		'W': grid[x, :y],
	}

	tree = []
	for direction, coords in directions.items():
		if direction == "W" or direction == "N":
			coords = coords[::-1]
		#Check to see if we've got a clear view
		#If so, add the length of the coords as we can see that far. 
		clear_view = coords < grid[x, y]
		if all(clear_view):
			tree.append(len(coords))

		else:
			#Now check where the first index that is greater than or equal to the grid.
			first_idx = np.where(coords >= grid[x,y])[0]
			tree.append(first_idx[0] + 1)

	return np.prod(tree)


def tree_calculator(grid:np.array, part:str):
	ht = grid.shape[0]
	wd = grid.shape[1]

	total_trees, high_score, tree_score = 0, 0, 0
	outer_ring = [0, int(ht-1), int(wd-1)]
	for x in range(wd):
		for y in range(ht):
			if x in outer_ring or y in outer_ring:
					total_trees += 1
					continue

			if part == 'part_A':
				if tree_is_visible(grid, x, y):
					total_trees += 1
					
			if part == 'part_B':			
				tree_score = calc_tree_score(grid, x, y) 
				if tree_score > high_score:
					high_score = tree_score
				
	if part == 'part_A':
		return total_trees
	if part == 'part_B':
		return high_score



@log_time
def run_part_A():
	grid = data_load()
	num_vis_trees = tree_calculator(grid, 'part_A')
	return num_vis_trees

@log_time
def run_part_B():
	grid = data_load()
	high_score = tree_calculator(grid, 'part_B')
	return high_score
	
print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")
