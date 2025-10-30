import random

rules = {
    'rock' : ['scissors', 'lizard'],
    'paper' : ['rock', 'spock'],
    'scissors' : ['lizard', 'paper'],
    'lizard' : ['spock', 'paper'],
    'spock' : ['rock', 'scissors']
}

CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')

player = input('Enter move: ')
computer = random.choice(CHOICES)

print(f'Your move: {player}')
print(f'Computer move: {computer}')
if computer in rules[player]:
    print('You win')
elif player in rules[computer]:
    print('You lose')
else:
    print('Its a tie')