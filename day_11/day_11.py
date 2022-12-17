import os
import sys
from collections import defaultdict
import operator
from math import prod

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
					'items': [int(x) for x in data[idx + 1].split(":")[1].strip().split(',')],
					'ops': data[idx + 2].split("=")[1].strip(),
					'test':data[idx + 3].split(":")[1].strip(),
					'True':data[idx + 4].split(":")[1][10:],
					'False':data[idx + 5].split(":")[1][10:],
					'insp_cnt': 0
				}
	return monkey_book


operations = {
	'*': operator.mul,
	'divisible': operator.truediv,
	'+': operator.add,
	'-': operator.sub
}

def adjust_worry(toss, ops, operations):
	left, op, right = ops.split()

	#cases for ops
	if left.isalpha() and right.isalpha():
		return operations[op](toss, toss)

	elif left.isalpha() and right.isdigit():
		return operations[op](toss, int(right)) 

	else:
		raise ValueError(f'Your input is corrupted')

def monkey_mania(monkey_book:dict, rounds:int, part, divid):
	#Our job here is to count the number of times a monkey inspects something. 
	#Order of operaions. 

	#Each monkey will go through every item in their list. 
		#They do an operation on the item to adjust the worry level
		#Then checks if its divisible by the test

	#After each monkey has gone through their list, the next monkey goes
	#when all monkeys go through their items, its a round
	#we're going through 20 rounds of this. 

	#For part B, take the modulo of the adjusted worry by the greatest common
	#denominator of the possible divisors. Which is all the divisors mutiplied
	#together in a set.

	
	# tst_range = list(range(0, 10_000, 1000))
	# tst_range.pop(0)
	# tst_range.insert(0, 20)
	# tst_range.insert(0, 1)
	divisor = prod(set([int(monkey_book[x]['test'].split()[2]) for x, y in monkey_book.items()])) 

	for round in range(rounds):
		# if round in tst_range:
		# 	print(f'round {round}')
		# print([monkey_book[x]['insp_cnt'] for x, y in monkey_book.items()])
		for monkey in monkey_book.keys():
			if len(monkey_book[monkey]['items']) == 0:
				continue

			while monkey_book[monkey]['items']:
				toss = monkey_book[monkey]['items'].pop(0)
				worry_adjust = adjust_worry(toss, monkey_book[monkey]['ops'], operations)
				if divid == 3:
					worry_adjust //= divid
				else:
					worry_adjust = worry_adjust % divisor

				if worry_adjust % int(monkey_book[monkey]['test'].split()[2]) == 0:
					monkey_book[monkey_book[monkey]['True']]['items'].append(worry_adjust)
				else:
					monkey_book[monkey_book[monkey]['False']]['items'].append(worry_adjust)
				
				monkey_book[monkey]['insp_cnt'] += 1

	top_two = sorted(monkey_book.items(), key = lambda x: x[1]['insp_cnt'])[-2:]
	top_two = [top_two[x][1]['insp_cnt'] for x in range(len(top_two))]
	return operations['*'](top_two[0], top_two[1])


@log_time
def run_part_A():
	monkey_book = data_load()
	rounds, part = 20, "part_A"
	monkey_biz = monkey_mania(monkey_book, rounds, part, 3)
	return monkey_biz


@log_time
def run_part_B():
	monkey_book = data_load()
	rounds, part = 10_000, "part_B"
	monkey_biz = monkey_mania(monkey_book, rounds, part, 1)
	return monkey_biz
	
# print(f"Part A solution: \n{run_part_A()}\n")
print(f"Part B solution: \n{run_part_B()}\n")

#Part A Notes.  

#These silly monkeys!  Seems as though they're tossing items around
#while we're hiking and we need to predict where the items go next.  

#Initial thoughts are using a dictionary of dicts with a operation function that
#magnifies the worry level.  Then perform a division test on the new worry level
#to decide where to throw the item.  If its a dict of lists, then i can just pop
#the items back and forth (ha!  probably what he intended there).  We need to
#keep track of what monkeys are doing what throwing too. So likely its good to
#have a dict key that serves as a counter for that




