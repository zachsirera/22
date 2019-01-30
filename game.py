# This is a program to play the game 22 in a python CLI format

import helpers 

# Create global variables needed
deck = []


# Create the necessary classes 
class player:

	# Initializer / Instance Attributes
    def __init__(hand, score):
        self.hand = hand
        self.score = score


