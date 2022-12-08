import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

def data_load()->str:
	# ./day6/
	with open('./day6/data.txt', 'r') as f:
		data = f.read()
	return data


def find_that_packet(data:str, offset:int):
	for x in range(len(data)):
		if len(set(data[x:x+offset])) == offset and x > 2:
			return x + offset

@log_time
def run_part_A():
	data = data_load()
	packet_start = find_that_packet(data, 4)
	return packet_start

@log_time
def run_part_B():
	data = data_load()
	packet_start = find_that_packet(data, 14)
	return packet_start
	
print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")

#Notes

#Goal.
#We're given one long big string. 
#We need to find the start of each packet.  A packet is defined as 4 unique characters. 

#Part A
#We want to know how far in does the packet start on test_data.txt

