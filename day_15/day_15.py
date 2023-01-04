#Beacon Exclusion Zone

import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

def data_load()->list:
	# ./day/
	with open('./day_15/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [tuple(line.split(":")) for line in data]
		sensors = [tuple(line[0].split(",")) for line in arr]
		beacons = [tuple(line[1].split(",")) for line in arr]
		sensors = [(int(sensors[x][0].split("=")[1]), int(sensors[x][1].split("=")[1])) for x in range(len(sensors))]
		beacons = [(int(beacons[x][0].split("=")[1]), int(beacons[x][1].split("=")[1])) for x in range(len(beacons))]

	return sensors, beacons
		
def manhattan(p1:tuple, p2:tuple)->int:
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def calc_part_A(sensors:list, beacons:list)->int:

	EVAL_Y = 2_000_000
	# EVAL_Y = 10

	#Iterate the sensor beacon pairs. 
	blocked, test = set(), set()
	for sensor, beacon in zip(sensors, beacons):
		#Calculate the manhattan distance
		dist_beacon = manhattan(sensor, beacon)

		#Examine the difference between the sensors y (row) and EVAL_Y
		y_diff = abs(sensor[1] - EVAL_Y)
		
		#since we just want to know how many are possible in that row, 
		#we look out in each direction the difference of the manhatten distance
		#stepwise and vertical row distance of the sensor to the evaluation row. 
		# If the difference is less than the manhattan distance,
			#It will have qualifying blocked cells in relation to the EVAL_Y 

		#If that is less than the manhattan distance.
		#Scan the difference of the manhatten left and right
		#to add the coverage of that diamond.

		if y_diff <= dist_beacon:
			scan = dist_beacon - y_diff
			for x in range(sensor[0] - scan, sensor[0] + scan + 1):
				blocked.add((x, EVAL_Y))

	#remove the sensor locations in blocked for a valid count via set membership test
	return len(blocked - set(beacons))

def calc_part_B(sensors:list, beacons:list)->int:

	EVAL_LOW = 0
	# EVAL_HIGH = 20
	EVAL_HIGH = 4_000_000

	for eval_y in range(EVAL_LOW, EVAL_HIGH + 1):
		blocked = []
		#Iterate the sensor beacon pairs. 
		for sensor, beacon in zip(sensors, beacons):
			#Calculate the manhattan distance
			dist_beacon = manhattan(sensor, beacon)

			#Examine the difference between the sensors y (row) and EVAL_Y
			y_diff = abs(sensor[1] - eval_y)

			#Now find the x component of that difference in sensors. 
			xscan = dist_beacon - y_diff

			# If its greater/= zero, add the range to the blocked list
			if xscan >= 0:
				blocked.append((sensor[0] - xscan, sensor[0] + xscan))

		blocked.sort()
		t_rng = blocked[0]
		for idx in range(1, len(blocked)):
			if blocked[idx][0] <= t_rng[1]:
				print("position", (t_rng[1], eval_y))
				t_rng = (t_rng[0], max(t_rng[1], blocked[idx][1]))
			else:
				return (t_rng[1] + 1)*4_000_000 + eval_y
			

@log_time
def run_part_A():
	sensors, beacons = data_load()
	num_sig_blocks = calc_part_A(sensors, beacons)
	return num_sig_blocks

@log_time
def run_part_B():
	sensors, beacons = data_load()
	tuning_freq = calc_part_B(sensors, beacons)
	return tuning_freq

print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")