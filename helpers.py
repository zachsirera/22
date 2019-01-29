# This file extends application.py 

import random
import math

# Create global variables that may be needed for the game
deck = []
hand1 = []
hand2 = []
hand3 = []
hand4 = []

def generate_deck():
	''' This is a function to create a deck, ie a list of dicts with values corresponding to card values.
	In the game 22, the suit of the card does not matter, only the value. '''

	global deck 
	suits = 4
	deck_len = 52
	cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

	for i in range(1, deck_len + 1):

		card = {
			str(i): cards[math.ceil(i / 4) - 1]
		}
		deck.append(card)

	return deck


def deal(players, cards):
	''' This is a function to deal cards to players based on the outcome of the previous half as well as the number of players. '''

	global deck
	min_cards = 5

	if players == 4:
		max_cards = 7
	else:
		max_cards = 11

	if cards > min_cards and cards < max_cards:
		deal_cards = cards
	elif cards < min_cards:
		deal_cards = min_cards
	else:
		deal_cards = max_cards

	for i in range(1, deal_cards):
		for j in range(1, players):
			card_value = random.randint(1, len(deck))

			card = deck[card_value]
			# deck.pop(card_value)
			print(card)
		


			
generate_deck()
print(deck)
deal(4, 5)

print(deck)





