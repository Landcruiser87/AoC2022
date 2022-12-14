#--- Day 10: Cathode-Ray Tube ---

import os
import sys
from collections import deque

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

def data_load()->list:
	# ./day10/
	with open('./day_10/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [tuple(x.split()) for x in data]
	return arr

def calc_part_A(data:list):
	register = 1
	cycle_c = sig_strength = 0
	sig_marker = list(range(20, 260, 40))
	com_que = deque(data)	
	
	while com_que:
		command = com_que.popleft()
		if command[0] == 'noop':
			cycle_c += 1
		else:	
			cycle_c += 2

		if any(cycle_c >= x for x in sig_marker if sig_marker):
			sig_strength += sig_marker[0]*register
			sig_marker.pop(0)

		if command[0] != 'noop':
			register += int(command[1])

	return sig_strength

def calc_part_B(data:list):
	#Draws a single pixel per cycle.  
	#Check to see if the register is in a position of 
	#a multiple of 40

	register = 1
	cycle_c = 0
	com_que = deque(data)
	sprite = []


	while com_que:
		command = com_que.popleft()
		if command[0] == 'noop':
			sprite.append(register)
			cycle_c += 1
			
		else:
			sprite.extend([register, register])
			cycle_c += 2
			register += int(command[1])


	for idx, reg in enumerate(sprite):
		pos = idx % 40
		
		if pos in [reg-1, reg, reg+1]:

			print('#', end="")
		else:
			print('.', end="")

		if pos == 39:
			print()



@log_time
def run_part_A():
	data = data_load()
	sig_sum = calc_part_A(data)
	return sig_sum

@log_time
def run_part_B():
	data = data_load()
	calc_part_B(data)

print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")

#Notes

#PartA

#So we're recalculating a display by tracking a series of commands that come from
#the cpu of the device.  
#It displays only one register number X
#X starts at 1

#the CPU has 2 commands
	#-addx (int)
	#noop

	#1. addx V
	# 	-each addx (int) takes 2 cycles to complete
	# 	-then adds/subtracts the signal number. 

	#2. noop
	#	-takes one cycle to complete. It has no other effect.
