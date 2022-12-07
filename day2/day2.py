#Rock Paper Scissors
#Day 2

import logging
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from utils.time_run import log_time

shape_score_dict = {
	"rock":1,
	"paper":2,
	"scissors":3
}

outcome_dict = {
	"loss":0,
	"draw":3,
	"win":6
}

player1_dict = {
	"A":"rock",
	"B":"paper",
	"C":"scissors"
}
game_dict = {
	("rock","scissors"):"win",
	("rock", "paper"):"loss",
	("rock", "rock"):"draw",
	("paper", "rock"):"win",
	("paper", "scissors"):"loss",
	("paper", "paper"):"draw",
	("scissors","paper"):"win",
	("scissors","rock"):"loss",
	("scissors","scissors"):"draw"
}


def data_load()->list:
	# ./day2/
	with open('./day2/data.txt', 'r') as f:
		data = f.read().splitlines()
		arr = [tuple(line.split(" ")) for line in data]
	return arr
	#Notes
	#Want to load the data as......
	# list of tuples??? Makes some sense.

def ca(arr)->int:
	player2_dict = {
		"X":"rock",
		"Y":"paper",
		"Z":"scissors"
		}
	p2_score = 0
	for game in range(len(arr)):
		outcome = game_dict[player2_dict[arr[game][1]], player1_dict[arr[game][0]]]
        logging.info(f"outcome: {outcome}")
		p2_score += shape_score_dict[player2_dict[arr[game][1]]] + outcome_dict[outcome]

	return p2_score

def calc_score_partB(arr)->int:
	player2_dict = {
		"X":"loss",
		"Y":"draw",
		"Z":"win"
	}

	p2_score = 0
	for game in range(len(arr)):
		outcome = player2_dict[arr[game][1]]
		player1_play = player1_dict[arr[game][0]]
		mini_dict = {k:v for k, v in game_dict.items() if v == outcome and k[1] == player1_play}
		player2_play = list(mini_dict.keys())[0][0]
		p2_score += shape_score_dict[player2_play] + outcome_dict[outcome]

	return p2_score

@log_time
def ra():
	data = data_load()
	total_score = ca(data)
	return total_score

@log_time
def run_part_B():
	data = data_load()
	total_score = calc_score_partB(data)
	return total_score

print(f"Part A solution: \n{ra()}\n")
print(f"Part B solution: \n{run_part_B()}\n")

#Part A Notes
#Input is a strategy guide of you vs all the other elfs in a tourny
#Total score per line
	# (What hand you played + outcome of round (win/loss/draw))

#Gameplan
	#1. Make a list of tuples.
	#2. Iterate said list
	#3. Calc outcome of game and add to your total tally (point of exercise)

#Part B Notes
#Ok this drunk elf is out of his mind.  The second column is apparently the encoded
#outcome for what should happen.  So you need to write a secondary function with the same loop
#just different inputs.  Could code it into one scoring function, but easier to make it 2
