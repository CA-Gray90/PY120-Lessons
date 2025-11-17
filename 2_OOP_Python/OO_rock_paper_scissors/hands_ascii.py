import os
import time

rock = [
    "    ____",
    "---'  | =|__",
    "      (_ )__)",
    "   __/(______)",
    "      (_____)",
    "---.__(____)",
    "    ROCK!"
]

paper = [
    "    ______",
    "---'    ___)___",
    "          ______)",
    "   __/     ______)",
    "       (   _____)",
    "---.__ ( ____)",
    "    PAPER!"
]

scissors = [
    "    ____",
    "---'  | =|_____",
    "      (_ )______)",
    "   __/  _________)",
    "       (___)",
    "---.__ (__)",
    "   SCISSORS!"
]

lizard = [
    "    ___",
    " ./    ``-___",
    "/   .-```--___)",
    "    |-__ '' _)",
    "         __'",
    "---.__ /",
    "   LIZARD!"
]

spock = [
    "    ____",
    "---'  | =|_____",
    "      (_ )______)",
    "   __/ (___)",
    "       ( __)_",
    "---.__  ______)",
    "    SPOCK!"
]

def display_hands(hands):
    for hand in hands:
        os.system('clear')
        for line in hand:
            print(line)
        time.sleep(0.75)

display_hands(rock, paper, scissors, lizard, spock)