'''
Keep score PEDAC

P:
Need a way to keep score for both player and computer. Must also display the
score. 

A full game is first to 3.

The program must end after 1 full game. Play again can be asked after each match

i:

o:

reqs:
- Don't use global variabels or class variables
- 

E:


D;


notes:
- Perhaps each Player class keeps track of its own score?
- Dont need a method to reset it since we only play one game
- Need a method to check for an overall winner, game must end once we have a
overall winner
- Need a method to display the score
- method to display overall score

A:
> While there is no overall winner:

    - display the score of both players
    - Play a match, update the scores


- display the scores
- display the overall winner
- Goodbye message

PCODE:
keep_playing = True

while keep_playing:
    display_score()
    play_match()

    if is_overall_winner:
        keep_playing = False

display_score()
display_overall_winner()
display_goodbye_msg()

c?
'''

class Player:
    def __init__(self):
        self._score = 0
    
    @property
    def score(self):
        return self._score
    
    def add_point(self):
        self._score += 1

player1 = Player()
print(player1.score)
player1.add_point()
print(player1.score)
player1.add_point()
print(player1.score)
player1.add_point()
print(player1.score)
player1.add_point()
print(player1.score)