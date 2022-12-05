import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

def data_load()->list:
	# ./day4/
	with open('./day4/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [tuple(x.split(',')) for x in data]
	return arr

def calc_over_lapping_pairs(data:list,part:str)->int:
	pair_count = 0
	for pair in range(len(data)):
		left_elf = data[pair][0].split("-")
		right_elf = data[pair][1].split("-")
		
		left_elf_rng = set(range(int(left_elf[0]), int(left_elf[1])+1))
		right_elf_rng = set(range(int(right_elf[0]), int(right_elf[1])+1))

		if part == 'part_A':
			#Test for set membership in either direction
			if left_elf_rng <= right_elf_rng or right_elf_rng <= left_elf_rng:
				pair_count += 1
		if part == 'part_B':
			#If anything is returned from intersection check, add to the count
			if left_elf_rng & right_elf_rng:
				pair_count += 1
	return pair_count

@log_time
def run_part_A():
	data = data_load()
	total_pairs = calc_over_lapping_pairs(data, 'part_A')
	return total_pairs

@log_time
def run_part_B():
	data = data_load()
	total_pairs = calc_over_lapping_pairs(data, 'part_B')
	return total_pairs
	
print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")

#Notes

#Part A 
#Goal 
#Count the number of overlapping ranges in the pairs. 
#Just need to test if one range is fully located iwthin another. 
#Use set memberships, remember to increase the right range by 1

#Part B
#Same but now we're lookign for any commonality.  
#Use set intersection as a boolean for counter.
