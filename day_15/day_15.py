#Beacon Exclusion Zone

import os
import sys
import numpy as np


root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

def data_load()->list:
	# ./day/
	with open('./day_15/test_data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [tuple(line.split(":")) for line in data]
		sensors = [tuple(line[0].split(",")) for line in arr]
		beacons = [tuple(line[1].split(",")) for line in arr]
		sensors = [(int(sensors[x][0].split("=")[1]), int(sensors[x][1].split("=")[1])) for x in range(len(sensors))]
		beacons = [(int(beacons[x][0].split("=")[1]), int(beacons[x][1].split("=")[1])) for x in range(len(beacons))]

	return sensors, beacons
		
def manhattan(p1:tuple, p2:tuple)->int:
	return abs(p1[0] - p2[0]) + abs(p1[1] -p2[1])

def calc_part_A(sensors:list, beacons:list)->int:

	# eval_row = 2_000_000
	eval_row = 10

	#Gameplan
	#Calculate the manhattan dist from sensor to beacon.
	#Generate a range up, down left right at that distance to beacon.
	#Calculate the manhattan dist for each point in that block range.
		#If the m_dist is less than the m_dist, add it to to the 
		#blocked set list.  
	
	#Iterate the sensor beacon pairs. 
	blocked, test = set(), set()
	for sensor, beacon in zip(sensors, beacons):
		#Calculate the manhattan distance
		dist_beacon = manhattan(sensor, beacon)

		#Generate x and y ranges that extend out NSEW the range of dist_beacon
		dirs = [range(sensor[0] - dist_beacon, sensor[0] + dist_beacon),
				range(sensor[1] - dist_beacon, sensor[1] + dist_beacon)	
			 ]

		#Iterate each cell in the dirs block to test if the manhattan distance
		#is less than or equal to dist_beacon
		for row in dirs[0]:
			for col in dirs[1]:
				if manhattan(sensor, (row, col)) <= dist_beacon:
					blocked.add((row, col))
					# if sensor == (8, 7):
					# 	test.add((row, col))

				# print(row, '\t', col)

	return len([tup for tup in blocked if tup[0]==eval_row])



@log_time
def run_part_A():
	sensors, beacons = data_load()
	num_sig_blocks = calc_part_A(sensors, beacons)
	return num_sig_blocks

@log_time
def run_part_B():
	data = data_load()
	
print(f"Part A solution: \n{run_part_A()}\n")
# print(f"Part B solution: \n{run_part_B()}\n")