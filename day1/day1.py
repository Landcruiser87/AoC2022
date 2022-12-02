import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time


def data_load()->list:
	# ./day1/
	with open('./day1/test_data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [int(x) if x != "" else "" for x in data]
	split_arr, curr_row = [], []

	# Testing a faster cleaner way to do this. Not sure i like the solution i came up with.  Lol. 
	# def split_list_on_space(empty_idx:list, arr:list):
	# 	for x in range(len(arr)):
	# 		if x in iter(empty_idx):
	# 			sub_list = arr[x:next(x, len(arr))]
	# 			yield sub_list


	# empty_idx = [idx for idx, value in enumerate(arr) if value == ""]
	
	# split_arr = list(split_list_on_space(empty_idx, arr))

	# return split_arr

	for x in range(len(arr)):
		if isinstance(arr[x], int):
			curr_row.append(arr[x])
			if x + 1 == len(arr) and len(curr_row) > 0:
				split_arr.append(list(curr_row))

		elif isinstance(arr[x], str):
			split_arr.append(list(curr_row))
			curr_row = []

	return split_arr

@log_time
def run_part_A():
	data = data_load()
	calories = [sum(x) for x in data]
	max_elf_sum = max(calories)
	return max_elf_sum

@log_time
def run_part_B():
	data = data_load()
	top3_calories = sorted([sum(x) for x in data])[-3:]
	return sum(top3_calories)
	
print(f"Part A solution: \n{run_part_A()}\n")

print(f"Part B solution: \n{run_part_B()}\n")

