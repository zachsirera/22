# This is a program to play the game 22 in a python CLI format

import helpers 

# Create global variables needed
deck = []
hands = []

# Initialize players scores
score1 = 0
score2 = 0
score3 = 0
score4 = 0


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

	# Execute the initial deal
	hands = helpers.deal(players, deal_cards)

	# Display each player's hand and allow them to dealback 
	for i in range(players):
		helpers.display_hand(hands[i])
		dealback_string = input('Please enter the indices of the cards ( eg. 135 ) you would like to return in the dealback.')

		for index in dealback_string:
			index_string = str(index)
			hands[i].pop(index_string - 1)

		dealback = helpers.dealback(len(dealback_string)) 

		new_hand = hands[i] + dealback

		print('Here is your new hand: ')
		helpers.display_hand(new_hand)

		move_on = input('Enter "y" when you are ready to move on to the next player.')

		if move_on == "y":

		





if __name__ == "__main__":
	game()
