# This is a program to play the game 22 in a python CLI format

import helpers 

# Create global variables needed
deck = []

hands = []


# Create the necessary classes 
class player:

	# Initializer / Instance Attributes
    def __init__(hand, score):
        self.hand = hand
        self.score = score


def game():
	''' This is a function to play the game of 22 '''

	global deck
	global hands

	# Get the number of players from CLI input
	players = helpers.get_players()

	# Generate the deck
	deck = helpers.generate_deck()

	# For the first hand, 7 cards are dealt.
	deal_cards = 7

	hands = helpers.deal(players, deal_cards)

	for i in range(1, players):
