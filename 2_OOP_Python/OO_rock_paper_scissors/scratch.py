score = {
    'player1' : {'points' : 3,
                 'history' : ['scissors', 'paper', 'rock']},
    'computer' : {'points' : 0,
                  'history' : ['paper', 'rock', 'scissors']}
}

def _display_history(score):
    for player in score.keys():
        print(player)
        print('Points:', score[player]['points'])
        print('Moves:')
        for move in score[player]['history']:
            print('   -', move)
        print()

_display_history(score)