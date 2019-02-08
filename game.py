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

	# Create player objects and initialize score. Yes this is ugly. 
	player1 = player(hands[0], 0)
	player2 = player(hands[1], 0)

	if players >= 3:
		player3 = player(hands[2], 0)

	if players == 4:
		player4 = player(hands[3], 0)

	print(chr(27) + "[2J")

	# Generate the deck
	deck = helpers.generate_deck()


	# For the first hand, 7 cards are dealt.
	deal_cards = 7

	while player1.score < 22 and player2.score < 22 and player3.score < 22 and player4.score < 22:

		# Execute the initial deal
		hands = helpers.deal(players, deal_cards)

		# Display each player's hand and allow them to dealback 
		for i in range(players):
			helpers.display_hand(hands[i], i + 1)
			dealback_string = input("Please enter whether you would like to keep each card ( eg. ynnynyy): ")

			if len(dealback_string) != len(hands[i]):
				dealback_string = input("Please enter whether you would like to keep each card ( eg. ynnynyy): ")
			else: 

			for j in dealback_string:
				if 

			# Reverse the dealback_string to use pop without error
			new_db_string = reversed(dealback_string)

			# Remove the cards from the user's hand 
			for j in new_db_string: 
				hands[i].pop(int(j) - 1)

			helpers.display_hand(hands[i], i + 1)

			# Call the dealback function to get new cards for the player
			dealback = helpers.dealback(len(dealback_string)) 

			# Concatenate the player's hand with their dealback, creating their final hand
			new_hand = hands[i] + dealback

			# Display the hand to the user
			helpers.display_hand(new_hand, i + 1)

			# Move on to the next player once the player is finished with the dealback.
			move_on = input('Enter "y" when you are ready to move on to the next player.')

			if move_on == "y":
				pass

		lead()
			





if __name__ == "__main__":
	game()
