import os
import time
import json

# tic = [
#     r' _____ _',
#     r"|_   _(_) ___",
#     r'  | | | |/ __|',
#     r'  | | | | (__',
#     r'  |_| |_|\___|',
# ]

# tac = [
#     r' _____ _        _____',
#     r"|_   _(_) ___  |_   _|_ _  ___",
#     r'  | | | |/ __|   | |/ _` |/ __|',
#     r'  | | | | (__    | | (_| | (__',
#     r'  |_| |_|\___|   |_|\__,_|\___|',
# ]

# toe = [
#     r' _____ _        _____            _____          _*',
#     r"|_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___| |",
#     r'  | | | |/ __|   | |/ _` |/ __|   | |/ _  \/ _ \ |',
#     r'  | | | | (__    | | (_| | (__    | | (_) |  __/_|',
#     r'  |_| |_|\___|   |_|\__,_|\___|   |_|\___/ \___(_)',
# ]

with open('TTT_Title.json', 'r') as file:
    tictactoe = json.load(file)
    
tic, tac, toe = tictactoe['tic'], tictactoe['tac'], tictactoe['toe']

for word in (tic, tac, toe):
    os.system('clear')
    for line in word:
        print(line)
    time.sleep(0.5)