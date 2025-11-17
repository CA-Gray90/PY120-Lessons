class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

human = Player('Human', 2)
computer = Player('Computer', 3)

def _display_scoreboard(human, computer):
    lines = [
        f'{human.name} : {human.score}',
        f'{computer.name} : {computer.score}'
    ]
    
    display_length = len(max(lines, key=len)) + 2
    boarder = '+' + ('-' * display_length) + '+'
    
    print(boarder)
    for line in lines:
        print(f'| {line.ljust(display_length - 1, ' ')}|')
    print(boarder)

_display_scoreboard(human, computer)