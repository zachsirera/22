#!/usr/bin/env python


# This is a program to play the game 22 among only AI players
# See the README.md for more information

import helpers 
import ai1 as player1
# import ai2
# import ai3
# import ai4



# Create the necessary classes

# Player object to track hand and scores of each player. 
class player:

	# Initializer / Instance Attributes
	def __init__(self, name, hand, score):
		# Important information: player's id, their hand, and their aggregate score for tracking in-game.
		self.name = name
		self.hand = hand
		self.score = score

# Outcome object to track who wins a hand under what circumstances. This will be used for strategy comparison.
class outcome:

	# Initializer / Instance Attributes
	def __init__(self, loser, leader, players, card):
		# Important information: who lost the hand, who lead, how many players were there, and what was the losing card.
		self.loser = loser
		self.leader = leader
		self.players = players
		self.card = card



def game_deal(players, cards):
	pass

def game_turn():
	pass


def game():
	''' This is a function to initiate the game process for a game involving all AI players '''

	pass

	# game_deal_ai()
	# while cards_left != 1:
	# 	game_turn_ai()
	# else:
	# 	loser = 
	# 	leader = 
	# 	players =
	# 	card =
	# 	hand_outcome = outcome(loser, leader, players, card)

	# 	# Append this to the outcome list.
	# 	outcome_list.append(hand_outcome)