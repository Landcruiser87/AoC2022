import os
import sys
from collections import defaultdict

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time


def data_load()->list:
	# ./day/
	with open('./day7/data.txt', 'r') as f:
		data = f.read().splitlines()

	# Guessing a dictionary of lists would be best to house this.
	#Logic is going to suck

	file_dict = defaultdict(list)
	f_path = ()
	

	for line in data:
		if line.startswith('$'):
			# print('give command')
			list_files = False
			command = line[2:4]
			#These are all the change directory commands. 
			#ie will change the curr_pos path. 
			if command == 'cd':
				direction = line[5:]

				if direction == "..":  #ie -Move up a directory
					f_path = f_path[:-1]
				else:
					n_path = f_path + (direction,)
					file_dict[f_path].append(n_path)
					f_path = n_path
					continue

			elif command == 'ls':
				list_files = True
				# print('listing files')
				continue
			
		if list_files:
			#Look for directory
			if line[0].isalpha():
				# print('add folder path')
				_, d_name = line.split()
				file_dict[f_path].append(d_name)

			#Look for file/filesize
			if line[0].isdigit():
				size, f_name = line.split()
				# print("add file")
				file_dict[f_path].append(int(size))
	return file_dict

def calc_part_A(file_dict, f_path):
	#Recursion to extract directory sizes. 
	dir_size = 0
	for dir_file in file_dict[f_path]:
		if isinstance(dir_file, int):
			dir_size += dir_file
		else:
			dir_size += calc_part_A(file_dict, dir_file)
	
	return dir_size

def calc_part_B(size_dict):
	hd_size = 70_000_000
	update_size = 30_000_000
	hd_used = size_dict[list(size_dict.keys())[0]]
	available = hd_size - hd_used
	min_size = update_size - available

	contenders = {}
	for path in size_dict.keys():
		if size_dict[path] > min_size: #size_dict[path] > available and 
			contenders[path] = size_dict[path]
	
	winner = min(contenders, key=contenders.get)
	return contenders[winner]

@log_time
def run_part_A():
	global B_dict
	data = data_load()
	dict_keys = list(data.keys())[1:]
	size_dict = {key:calc_part_A(data, key) for key in dict_keys}
	B_dict = size_dict.copy()
	[size_dict.pop(x) for x in dict_keys if size_dict[x] > 100_000]
	return sum(size_dict.values())

@log_time
def run_part_B():
	size_dict = B_dict
	dir_del_size = calc_part_B(size_dict)
	return dir_del_size

print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")

#Notes
#Now our goal shifts to some memory saving on the device the elves gave us 
#Our initial goal should be building a treemap of each directory, the files in it
#and the size of the directory.  (dataload)


#Part A
#Determine all the directories with a size above
