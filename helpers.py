# This file extends application.py 

import random

def make_deck():
	''' This is a program to create a deck, ie a list of dicts with values corresponding to card values.
	In the game 22, the suit of the card does not matter, only the value. '''

	deck = []
	suits = 4
	cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

	for i in range(len(cards)):
		for j in range(suits): 
			card = { 
				str((i - 1) * suits * j): str(cards[i])
			}
			deck.append(card)

	print(deck)
	return deck

	

def deal(players, cards):
	''' This is a function to deal cards to players based on the outcome of the previous half as well as the number of players. '''

	min_cards = 5

	if players == 4:
		max_cards = 7
	else:
		max_cards = 11

	if cards > min_cards && cards < max_cards:
		deal_cards = cards
	else if: cards < min_cards:
		deal_cards = min_cards
	else:
		deal_cards = max_cards

	for i in range(deal_cards):
		for j in range(players):
			card = random.randint(1, 53)

