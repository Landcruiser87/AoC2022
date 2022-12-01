def data_load()->list:
	# ./day1/
	with open('./day1/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [int(x) if x != "" else "" for x in data]
		split_arr, curr_row = [], []

	for x in range(len(arr)):
		if isinstance(arr[x], int):
			curr_row.append(arr[x])
			if x + 1 == len(arr) and len(curr_row) > 0:
				split_arr.append(list(curr_row))	
		elif isinstance(arr[x], str):
			split_arr.append(list(curr_row))
			curr_row = []

	return split_arr

data = data_load()

def run_part_A():
	data = data_load()
	calories = [sum(x) for x in data]
	max_elf_sum = max(calories)
	return max_elf_sum

def run_part_B():
	data = data_load()
	calories = sorted([sum(x) for x in data])[-3:]
	return sum(calories)
	

print(f"Solution for Part A: {run_part_A()}")

print(f"Solution for Part B: {run_part_B()}")

