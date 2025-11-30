# Defense:
'''
P:
If the player has 2 out of 3 in a combo to win, and the reamining square is empty,
the computer should choose to play the remaining square.

i:
- combo, tuple of 3 positions (ints)
    - e.g: 
        (1, 2, 3) # 1st row -> ('x', 'x', '')

o:
- Square or position to play? (from the above example: 3)

rules:
- Takes a combo, returns a position to play

E:
Given: ('x', '', 'x')
D:

notes:

A:
The method should be able to receive a combo, check how many marks in there are
the players, then if its 2 out of 3, return the move that the computer must play.

Otherwise it should return None

Then the computer will either choose the remaining square if the function returns
a value, else choose randomly as before. Computer turn method should be updated.

c?
'''

