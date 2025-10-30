import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')

    def __init__(self):
        self.move = None
        self._name = None
        self._score = 0

    @property
    def score(self):
        return self._score

    @property
    def name(self):
        return self._name

    def add_point(self):
        self._score += 1

class Computer(Player):
    def __init__(self):
        super().__init__()
        self._name = 'Computer Player'

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        super().__init__()
        self._name = 'Human Player'

    def choose(self):
        prompt = "Enter either 'rock', 'paper', 'scissors', 'lizard' or 'spock'"

        while True:
            move = input(f'{prompt}: ').lower()
            if move in Player.CHOICES:
                break

            print('Invalid input. ', end='')

        self.move = move

class RPSGame:
    POINTS_TO_WIN = 5
    RULES = {
        'rock' : ['scissors', 'lizard'],
        'paper' : ['rock', 'spock'],
        'scissors' : ['lizard', 'paper'],
        'lizard' : ['spock', 'paper'],
        'spock' : ['rock', 'scissors']
    }

    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_msg(self):
        print('Welcome to Rock Paper Scissors Lizard Spock!')

    def _display_goodbye_msg(self):
        print('Thanks for playing. Goodbye!')

    def _determine_round_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        if computer_move in RPSGame.RULES[human_move]:
            return self._human
        elif human_move in RPSGame.RULES[computer_move]:
            return self._computer
        else:
            return None

    def _display_winner(self):
        print(f'You chose: {self._human.move.capitalize()}')
        print(f'Computer chose: {self._computer.move.capitalize()}')

        winner = self._determine_round_winner()
        if winner == self._human:
            self._human.add_point()
            print('You win!')
        elif winner == self._computer:
            self._computer.add_point()
            print('Computer won. You lost!')
        else:
            print("It's a Tie!")

    def _display_overall_winner(self):
        if self._human.score == RPSGame.POINTS_TO_WIN:
            print('You are the overall winner!')
            return True
        elif self._computer.score == RPSGame.POINTS_TO_WIN:
            print('Computer is the overall winner!')
            return True
        else:
            return False
    
    def _display_scoreboard(self):
        print(f'{self._human.name} : {self._human.score}\n'
              f'{self._computer.name} : {self._computer.score}')

    def _play_again(self):
        prompt = 'Play again? (y/n)'

        while True:
            answer = input(f'{prompt}: ').lower()
            if answer in ('yes', 'no', 'y', 'n'):
                return answer[0] == 'y'

            print('Invalid input. ', end='')

    def _play_round(self):
        self._human.choose()
        self._computer.choose()
        self._display_winner()

        # Display scores:
        self._display_scoreboard()
        
    # Orchestration function to play the game
    def play(self):
        self._display_welcome_msg()

        while True:
            self._play_round()
            if self._display_overall_winner():
                if not self._play_again():
                    break

        self._display_goodbye_msg()

RPSGame().play()