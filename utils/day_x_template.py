import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

def data_load()->list:
	# ./day/
	with open('./day/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [int(x) if x != "" else "" for x in data]
	


@log_time
def run_part_A():
	data = data_load()


@log_time
def run_part_B():
	data = data_load()
	
print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")