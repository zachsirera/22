# This file extends game.py

import helpers

# This is an AI to play the card game 22. This AI adheres to a strict set of rules. Future AI players will invoke more complex decision matrices.

####### Rule outline: #######

## Deal Rules ##

# On initial deal, keep all: 2, 3, Q, K, A
# On initial deal, keep pairs: J
# On initial deal, keep triples: J, 10
# On initial deal, keep quads: J, 10, 9

## Lead Rules ##

# Always lead the lowest single "trash" card in the hand . A trash card is defined as a card not present in the "keep all" list.
# Once all trash cards are removed from the players hand, lead the lowest face value, highest multiple. IE, lead 3 9s before 2 10s.
# Once all multiples have been removed from the players hand, lead the lowest value single that is not a 2 or a 3.
# If the resulting hand from the lead is lower value than A, 2, 3, lead the second lowest single. 

## Play Rules ##

# Always play the lowest value single card that beats the current play on the table.
# Always play the lowest combination of multiples that beats the current play on the table. 
# Split high value pairs rather than playing a higher card. IE, if the hand contains QKKA, play QK instead of QA.
# If multiple low cards and few high cards, play under if the number of cards of the resulting hand minus 1 is greater than the 
# number of high cards. IE, hand: 23KA, Play a 2 to avoid being left in a 23A situation.





# This is a variable to test the functions. To be removed.
test_hand = [
	{"face": "2", "value": 2, "score_value": 2, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "3", "value": 3, "score_value": 3, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "4", "value": 4, "score_value": 4, "deal_2": 5, "deal_3": 5, "deal_4": 5},  
	{"face": "5", "value": 5, "score_value": 5, "deal_2": 5, "deal_3": 5, "deal_4": 5}, 
	{"face": "9", "value": 9, "score_value": 9, "deal_2": 9, "deal_3": 9, "deal_4": 7},
	{"face": "10", "value": 10, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7},
	{"face": "10", "value": 10, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7},
	{"face": "10", "value": 10, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7},
	{"face": "J", "value": 11, "score_value": 10, "deal_2": 10, "deal_3": 10, "deal_4": 7}
	]


####### Gameplay functions: #######


def toss(hand):
	''' This is a function to apply the rules listed above for the initial deal. '''

	# These cards are tossed no matter what
	toss_list = ['4', '5', '6', '7', '8']

	# Create a list that will make operations easier
	face_list = []
	for card in hand:
		face_list.append(card['face'])

	# Setup the necessary variables for the popping operation
	hand_len = len(face_list)
	rev_hand = reversed(face_list)

	# Pass through and remove the cards that are never kept
	for index, card in enumerate(rev_hand):
		if card in toss_list:
			face_list.pop(hand_len - 1 - index)

	# Pass through and remove cards that are not high value pairs
	if face_list.count('J') > 1:
		pass
	else:
		face_list = [x for x in face_list if x != 'J']

	# Pass through and remove cards that are not high value triplets
	if face_list.count('10') > 2:
		pass 
	else:
		face_list = [x for x in face_list if x != '10']

	# Pass through and remove cards that are not high value quads
	if face_list.count('9') > 3:
		pass 
	else:
		face_list = [x for x in face_list if x != '9']

	# Create and return hand based on remaining items in face_list
	new_hand = []
	for value in face_list:
		card = next((x for x in helpers.cards_list if x['face'] == value), None)
		new_hand.append(card)

	helpers.display_hand(new_hand, 1)
	return new_hand




def lead(hand):
	''' This is a function to apply the rules listed above for the lead '''
	
	trash_cards = ['5', '6', '7', '8', '9', '10', 'J']

	sorted_hand = sorted(hand, key=lambda k: k['value'])

	helpers.display_hand(trash_cards, 1)
	helpers.display_hand(sorted_hand, 1)
	
	for index, card in enumerate(sorted_hand):
		# Lead the lowest single trash card
		if card['value'] in trash_cards:
			lead = sorted_hand.pop(index)
			helpers.display_hand(lead, 1)
			helpers.display_play(lead)
			return lead
		# Lead the highest-order, lowest-value multiple
		else:
			pass
		# Lead any other multiple
		# Lead any single that is not a 2 or 3, as long as the resulting hand is not two low cards and an A.




def play(hand, current_play):
	''' This is a function to apply the rules listed above for playing in response to the current play '''
	pass



lead(test_hand)
