import random

class Move:
    def __init__(self):
        self._beats = None

    def __str__(self):
        return NotImplemented

    # Each Move subclass knows who it can beat (using comparison operators)
    def __gt__(self, other):
        if isinstance(other, Move):
            return str(other) in self._beats
        else:
            return NotImplemented

class Rock(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('scissors', 'lizard')

    def __str__(self):
        return 'rock'

class Paper(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('rock', 'spock')

    def __str__(self):
        return 'paper'

class Scissors(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('lizard', 'paper')

    def __str__(self):
        return 'scissors'

class Lizard(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('paper', 'spock')

    def __str__(self):
        return 'lizard'

class Spock(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('rock', 'scissors')

    def __str__(self):
        return 'spock'

class Player:
    CHOICES = (Rock(), Paper(), Scissors(), Lizard(), Spock())

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
        prompt = ("Enter either 'rock', 'paper', 'scissors', "
                  "'lizard' or 'spock'")

        while True:
            choice = input(f'{prompt}: ').lower()
            if choice in {str(move) for move in Player.CHOICES}:
                break

            print('Invalid input. ', end='')

        for move in Player.CHOICES:
            if str(move) == choice:
                self.move = move

class RPSGame:
    POINTS_TO_WIN = 5

    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_msg(self):
        print('Welcome to Rock Paper Scissors Lizard Spock!')
        print(f'First to {RPSGame.POINTS_TO_WIN} wins!')

    def _display_goodbye_msg(self):
        print('Thanks for playing. Goodbye!')

    def _determine_round_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        if human_move > computer_move:
            return self._human
        elif computer_move > human_move:
            return self._computer
        else:
            return None

    def _display_winner(self):
        print(f'You chose: {str(self._human.move).capitalize()}')
        print(f'Computer chose: {str(self._computer.move).capitalize()}')

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