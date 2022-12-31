import os
import sys
import numpy as np
from collections import deque



root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

def data_load()->list:
	# ./day/
	with open('./day_14/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [[tuple(coord.split(',')) for coord in line.split(' -> ')] for line in data]
		arr = [[tuple(map(int, coord)) for coord in line] for line in arr]		

	return arr

def onboard(data:np.array, x1:int, y1:int)->bool:
	ht = data.shape[0]
	wd = data.shape[1]
	if x1 < 0 or y1 < 0 or x1 >= ht or y1 >= wd:
		return False
	else:
		return True

def calc_part_A(data:list)-> int:
	#grid layout
	# # # # # # # 
	#x---------->
	#y#
	#|#
	#|#
	#|#
	#v# # # # # #
	
	#first get max/min of each grid
	max_x = max([max(line, key=lambda x:x[0]) for line in data], key=lambda y: y[0])[0]
	min_x = min([min(line, key=lambda x:x[0]) for line in data], key=lambda y: y[0])[0]
	max_y = max([max(line, key=lambda x:x[1]) for line in data], key=lambda y: y[1])[1]
	min_y = min([min(line, key=lambda x:x[1]) for line in data], key=lambda y: y[1])[1]
	ht = np.arange(0, max_y + 1)
	wd = np.arange(min_x, max_x + 1)

	grid = np.zeros(shape=(ht.size, wd.size), dtype='int')
	start = (0, np.where(wd==500)[0].item())

	#Iterate through the array and assign ones to all the rocks	
	for line in data:

		x_vals = [wd.tolist().index(x[0]) for x in line]
		y_vals = [y[1] for y in line]
		rockpile = deque(zip(x_vals, y_vals))

		while len(rockpile) > 1:
			c1, r1 = rockpile.popleft()
			c2, r2 = rockpile[0]

			if c2 < c1:
				c1, c2 = c2, c1
			if r2 < r1:
				r1, r2 = r2, r1

			grid[r1:r2+1, c1:c2+1] = 1
	
	poursand = True

	#Pour the sand
	while poursand:
		#isolate first row with a 1 and mark it from the drop.
		c_row = np.argmax(grid[:, start[1]]) - 1
		c_col = start[1]

		atrest = False
		while not atrest:
			for x in [-1, 1]:
					if not onboard(grid, c_row + 1, c_col + x):
						poursand = False
						break

			#check to see if diag lower left is availble
			if not poursand:
				break

			if grid[c_row + 1, c_col] == 0:
				c_row += 1

			elif grid[c_row + 1, c_col - 1] == 0:
				c_col -= 1
				c_row += 1

			#check to see if diag lower right is avaible
			elif grid[c_row + 1, c_col + 1] == 0:
				c_col += 1
				c_row += 1

			else:
				atrest = True

		if poursand:
			grid[c_row, c_col] = 2

	return np.where(grid==2)[0].size


@log_time
def run_part_A():
	data = data_load() 
	num_grains = calc_part_A(data)
	return num_grains


@log_time
def run_part_B():
	data = data_load()
	
print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")