import os
import sys
from collections import defaultdict
import operator


root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

def data_load()->list:
	# ./day/
	#Dict of lists
	with open('./day_11/data.txt', 'r') as f:
		data = f.read().splitlines()
		monkey_book = defaultdict(dict)
		for idx, line in enumerate(data):
			if "Monkey" in line:
				monkey = line.lower().strip(":")
				monkey_book[monkey] = {
					'monkeybag': [int(x) for x in data[idx + 1].split(":")[1].strip().split(',')],
					'ops': data[idx + 2].split("=")[1].strip(),
					'test':data[idx + 3].split(":")[1].strip(),
					'True':data[idx + 4].split(":")[1][10:],
					'False':data[idx + 5].split(":")[1][10:],
					'insp_cnt': 0
				}
	#Possibly do the string adjustments in here. s

	return monkey_book

		#Read data in, 
		#split on newlines
		#lower the monkey and make it suitable for a keydict. 
		#assign dict values as such. 
		
def calc_part_A(monkey_book:dict):
	#Our job here is to count the number of times a monkey inspects something. 
	#Order of operaions. 

	#Each monkey will go through every item in their list. 
		#They do an operation on the item to adjust the worry level
		#Then checks if its divisible by the test

	#After each monkey has gone through their list, the next monkey goes
	#when all monkeys go through their items, its a round
	#we're going through 20 rounds of this. 

	operations = {
		'*': operator.mul,
		'divisible': operator.truediv,
		'+': operator.add,
		'-': operator.sub
	}

	def adjust_worry(toss, ops, operations):

		left, op, right = ops.split()
		#Cases for ops
		if left.isalpha() and right.isalpha():
			return operations[op](toss, toss) // 3

		elif left.isalpha() and right.isdigit():
			return operations[op](toss, int(right)) // 3
		else:
			raise ValueError(f'Your input is corrupted')
		

	for round in range(20):
		for monkey in monkey_book.keys():
			for toss in monkey_book[monkey]['monkeybag']:
				worry_adjust = adjust_worry(toss, monkey_book[monkey]['ops'], operations)
				if worry_adjust % int(monkey_book[monkey]['test'].split()[2]) == 0:
					monkey_book[monkey_book[monkey]['True']]['monkeybag'].append(worry_adjust)
				else:
					monkey_book[monkey_book[monkey]['False']]['monkeybag'].append(worry_adjust)

				
				monkey_book[monkey]['insp_cnt'] += 1
			monkey_book[monkey]['monkeybag'] = []
	
	top_two = sorted(monkey_book.items(), key = lambda x: x[1]['insp_cnt'])[-2:]
	top_two = [top_two[x][1]['insp_cnt'] for x in range(len(top_two))]
	return operations['*'](top_two[0], top_two[1])


@log_time
def run_part_A():
	monkey_book = data_load()
	monkey_biz = calc_part_A(monkey_book)
	return monkey_biz


@log_time
def run_part_B():
	data = data_load()
	
print(f"Part A solution: \n{run_part_A()}\n")
# print(f"Part B solution: \n{run_part_B()}\n")

#Part A Notes.  

#These silly monkeys!  Seems as though they're tossing items around
#while we're hiking and we need to predict where the items go next.  

#Initial thoughts are using a dictionary of dicts with a operation function that
#magnifies the worry level.  Then perform a division test on the new worry level
#to decide where to throw the item.  If its a dict of lists, then i can just pop
#the items back and forth (ha!  probably what he intended there).  We need to
#keep track of what monkeys are doing what throwing too. So likely its good to
#have a dict key that serves as a counter for that




