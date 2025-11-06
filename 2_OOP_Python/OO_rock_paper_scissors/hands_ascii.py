import os
import time

rock = [
    "    ____",
    "---'  | =|__",
    "      (_ )__)",
    "   __/(______)",
    "      (_____)",
    "---.__(____)",
]

paper = [
    "    ______",
    "---'    ___)___",
    "          ______)",
    "   __/     ______)",
    "       (   _____)",
    "---.__ ( ____)",
]

scissors = [
    "    ____",
    "---'  | =|_____",
    "      (_ )______)",
    "   __/  _________)",
    "       (___)",
    "---.__ (__)",
]

lizard = [
    "    ___",
    " ./    ``-___",
    "/   .-```--___)",
    "    |-__ '' _)",
    "         __'",
    "---.__ /",
]

spock = [
    "    ____",
    "---'  | =|_____",
    "      (_ )______)",
    "   __/ (___)",
    "       ( __)_",
    "---.__  ______)",
]

def display_hands(*hands):
    for hand in hands:
        os.system('clear')
        for line in hand:
            print(line)
        time.sleep(0.5)

display_hands(rock, paper, scissors, lizard, spock)