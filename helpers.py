# This file extends game.py 

import random
import math

# Create global variables that may be needed for the game. This will eventually be made a little more OOP. 
deck = []

hand1 = []
hand2 = []
hand3 = []
hand4 = []
hands = []

deal_back =[]

score1 = 0
score2 = 0
score3 = 0
score4 = 0

def get_players():
	''' This is a function to ask the user how many players are playing. '''

	players = input('How many players will be playing, 2, 3, or 4?')

	if players > 4 or players < 2:
		print('Please select a number between 2 and 4.')
		get_players()
	else:
		return players





def generate_deck():
	''' This is a function to create a deck, ie a list of dicts with values corresponding to card values.

	In the game 22, the suit of the card does not matter, only the value. 

	This function takes no arguments and is called at the beginning of the hand. 

	When this function is called at the beginning of 
	the game, the cards are generated and a list of dicts is returned, numbered 1 to 52 and labeled with the card value.
	'''

	global deck 
	suits = 4
	deck_len = 52
	cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

	for i in range(1, deck_len + 1):

		card = {
			'card': cards[math.ceil(i / 4) - 1]
		}
		deck.append(card)

	return deck


def deal(players, cards):
	''' This is a function to deal cards to players for the coming hand.

	The game of 22 can be played with 2 to 4 players. If the hand is the first hand of the game everyone is dealt 7 cards.
	Otherwise, players are dealt the number of cards corresponding to the point value of the previous hand's losing card. 
	In other words, if a player loses with a 6, they deal 6 cards in the following hand. To conserve cards, in a 4 person game 
	this is capped at 7 cards to ensure that there are cards remaining in the deck to conduct at least a partial dealback. 

	As a card is "dealt" that dict is popped from the deck and the card is appending to a player's hand.

	The first argument is the number of players in the hand, the second argument is the number of cards to be dealt. This is 
	simply the points "taken" by the losing player of the previous hand. This number does not need to be sanitized. The function 
	will determine the proper amount of cards to deal if this is less than the minimum or greater than the maximum.

	When this function is called at the beginning of a hand, a list of lists is returned, where each sub-list corresponds to each 
	players hand. These hands are lists of the card values for each card. 


	'''

	global deck
	global hand1
	global hand2
	global hand3
	global hand4
	global hands

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

	for i in range(1, deal_cards - 1):
		for j in range(1, players + 1):

			card_value = random.randint(1, len(deck) - 1)
			card = deck[card_value]
			
			if j == 1:
				hand1.append(card['card'])
				deck.pop(card_value)
			if j == 2:
				hand2.append(card['card'])
				deck.pop(card_value)
			if j == 3: 
				hand3.append(card['card'])
				deck.pop(card_value)
			if j == 4:
				hand4.append(card['card'])
				deck.pop(card_value)

	if players >= 2:
		hands.append(hand1)
		hands.append(hand2)
	if players >= 3:
		hands.append(hand3)
	if players == 4:
		hands.append(hand4)

	return hands


def dealback(new_cards):
	''' This is a function to handle the dealback, a crucial element in a game of 22 

	In the game of 22, players have the option after the initial deal to "throw away" any of their cards and try
	to get better cards through the "dealback". For example, player 1 may want to discard 3 cards and receive 3 new cards. 

	The only argument this function takes is an int for the number of cards a player would like to receive back.

	This function will return exit code 1 if the player is requesting more cards than are available and will force them to 
	hold enough cards such that the new cards the player is requesting is less than or equal to the remainder of the deck.

	When this function is called a list is returned containing the card values of the new cards.

	'''

	global deck
	global deal_back

	if len(deck) < new_cards:
		exit(1)

	for i in range(new_cards):
		card_value = random.randint(1, len(deck))
		card = deck[card_value]
		deal_back.append(card['card'])
		deck.pop(card_value)

	return deal_back

def lead(leader):
	''' The lead is the play that starts the turn. The "leader" may choose how many cards to play. 

	In a turn, one player "leads". The leader may choose to play 1 to 4 cards. If a player leads more than 1 card, 
	they must be of the same value.

	This function takes one argument, an int representing which player is leading. 

	When called, this function returns a list containing the leader's lead.
	'''

	global hands

	hand = hands[leader]






def turn(play):
	''' 22 is a turn-based game where players play cards and one player wins the turn.  

	In a turn, one player "leads". The leader may choose to play 1 to 4 cards. If a player leads more than 1 card, 
	they must be of the same value. Though the leader may only lead 2, 3, or 4 of a kind, the players following are not required
	to play cards of the same value. To "beat" a lead, a player needs only to tie the cards played. A turn is over when all 4 
	players have played. The player who plays the highest card or cards will "win" the turn and lead the following turn. A player 
	who cannot beat the cards currently on the table has to play their lowest card(s) as penalty. A player may also choose to "play 
	under" strategically, where they willingly play their lowest card(s) to preserve the remainder of their hand. 

	This function takes one argument, the play of the player before as a list.

	When called, this function returns a list of the players play. 

	'''
	






		


			
# generate_deck()
# print(deck)
# deal(4, 5)

# print(hands[0])
# print(hands[1])
# print(hands[2])
# print(hands[3])

# print(len(deck))

get_players()





