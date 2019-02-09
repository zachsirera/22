#!/usr/bin/env python


# This is a program to play the game 22 in a python CLI format
# See the README.md for more information

import helpers 

# Create global variables needed
deck = []
hands = []


# Create the necessary classes 
class player:

	# Initializer / Instance Attributes
    def __init__(self, hand, score):
        self.hand = hand
        self.score = score


def game():
	''' This is a function to play the game of 22 '''

	# Recall the global variables
	global deck
	global hands


	# Get the number of players from CLI input
	players = helpers.get_players()


	# Generate the deck
	deck = helpers.generate_deck()


	# For the first hand, 7 cards are dealt.
	deal_cards = 7

	

	# Execute the initial deal
	hands = helpers.deal(players, deal_cards)

	# Create player objects and initialize score. Yes this is ugly. 
	player1 = player(hands[0], 0)
	player2 = player(hands[1], 0)

	if players >= 3:
		player3 = player(hands[2], 0)

	if players == 4:
		player4 = player(hands[3], 0)

	# Clear the screen
	print(chr(27) + "[2J")

	# Display each player's hand and allow them to dealback 
	for i in range(players):

		sortedhand = sorted(hands[i], key=lambda k: k['value'])

		helpers.display_hand(sortedhand, i + 1)

		dealback_string = input("Please indicate whether you would like to keep each card ( eg. ynnynyy): ")

		while len(dealback_string) != len(sortedhand):
			dealback_string = input("Please indicate whether you would like to keep each card ( eg. ynnynyy): ")
		else: 

			# Reverse order in order to perform popping operation without error
			rev_db_string = reversed(dealback_string)

			for index, j in enumerate(rev_db_string):
				if j == "n":
					sortedhand.pop(6 - index)
				
			# Get dealback cards 	
			dealback = helpers.dealback(deal_cards - len(sortedhand))

			# Concatenate the two lists
			new_hand = sortedhand + dealback

			# sort the new hand
			sorted_new_hand = sorted(new_hand, key=lambda k: k['value'])

			# Clear the screen
			print(chr(27) + "[2J")

			# Display the new hand
			helpers.display_hand(sorted_new_hand, i + 1)

			input("Press enter to move to the next player. ")

			# Clear the screen
			print(chr(27) + "[2J")








if __name__ == "__main__":
	game()
