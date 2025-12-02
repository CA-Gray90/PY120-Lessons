import os
import time
import json

def title_seq():
    with open('TTT_Title.json', 'r') as file:
        tictactoe = json.load(file)

    tic, tac, toe = tictactoe['tic'], tictactoe['tac'], tictactoe['toe']

    for word in (tic, tac, toe):
        os.system('clear')
        print(f'{'  Welcome to:  '.center(80, '*')}')
        print()
        for line in word:
            print(line.center(80, ' '))
        time.sleep(0.5)