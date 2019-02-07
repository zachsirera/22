# This is a program to play the game 22 with multiple players through a command line interface

The rules of 22 are simple. There is no winner, there is only a loser. 
The loser of each hand accumulates "points", and the first person to reach a cumulative score of 22 loses. 

A player loses a hand by getting to their last card and having it be higher in value than anyone else.

Each hand follows the same format. The "leader" starts off the hand by deciding to play 1, 2, 3, or 4 cards.
If the leader elects to play more than one card, they must be of the same number. 

The players then in clockwise order play on this lead. They may tie or beat the lead, or they are penalized 
and are forced to play their lowest card(s). 

After each player has played once, the last player to tie or beat the cards on the table wins the turn and 
gets to lead the following turn. They may again lead as many cards as their hand allows, provided they leave
at minimum one card remaining. 

This process repeats until the players are down to their last card, at which point a loser is chosen.

The loser then deals the following hand, unless their score is greater than or equal to 22.

More information can be found here: https://www.pagat.com/last/22.html 