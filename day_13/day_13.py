import os
import sys
import json
from collections import deque

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

def data_load()->list:
	# ./day_13/

	with open('./day_13/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [list(json.loads(line)) for line in data if len(line) !=0]				

	return arr

def compare(p1, p2)->bool:
	p1_type = isinstance(p1, int)
	p2_type = isinstance(p2, int)
	
	#First, check if both are ints. 
	if p1_type and p2_type:
		if p1 == p2:
			return 'gooseggs'
		if p1 < p2:
			return True
		if p1 > p2:
			return False
	
	#Now check if only one is an int.  recurse till both ints
	if (not p1_type or not p2_type):
		# if p1 is an int
		if p1_type:
			return compare([p1], p2)
		# if p2 is an int
		elif p2_type:
			return compare(p1, [p2])
		#both are lists
		for x, y in zip(p1, p2):
			mini_ver = compare(x, y)
			
			if mini_ver != 'gooseggs':
				return mini_ver

		return compare(len(p1), len(p2))

def calc_part_A(data)->int:
	inorder = []

	for line in range(0, len(data), 2):
		p1 = data[line]
		p2 = data[line + 1]
		inorder.append(compare(p1, p2))

	return sum([idx+1 for idx, x in enumerate(inorder) if x == True])
		
def calc_part_B(pairs)->int:
	#multiply the indexes of the divider packets
	div_one = [[2]]
	div_two = [[6]]

	#compare div_one to each index.  If its greater than that index,
	#add a 1 to the list, then sum them up to see how far it got into the
	#list

	first_div = sum([1 for x in pairs if compare(x, div_one)])
	sec_div = sum([1 for x in pairs if compare(x, div_two)])

	return first_div * sec_div



@log_time
def run_part_A():
	data = data_load()
	pair_count = calc_part_A(data)
	return pair_count	

@log_time
def run_part_B():
	data = data_load()
	data.extend([[[2]], [[6]]])
	decoder_key = calc_part_B(data)
	return decoder_key

print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")

#Part A Notes. 

#Each packet comes in on its own line
#packets are grouped into 2 lines.  
#Both lines in the right order = valid packet
#We have to sum the indices of the valid packets.

#Our job is to compare the packets to how many *pairs* are in the right order.
#They're all a bunch of lists or integers but in random shapes it looks like. 

#Operations
#each comparison has a left and a right
	#if both values are ints
		#if the left is lower than the right = right order
		#if left is higher than right, out of order. 
			#maybe try a while boolean false flag
		#Otherwise, inputs are the same integer. 
			#continue to the next comparison
			#meaning put a continue in there for this condition. 

	# if both vals are lists
		#compare the first val of each list, then the second and so on. 
		#if the left list runs out of items first = right order
		#if the righ list runs out of items first = out of order. 
		#if lists are same length and no comparison makes a decision about order
			#continue
	
	#if exactly??? one val is an int.
		#convert the int to a list which contains that int as its only val and retry comparison
		#Ah meaning if a value is a single val and doesn't have brackets, 
		#make it a list to do the comparison. 

			