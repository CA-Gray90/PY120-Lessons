import random

class Move:
    def __init__(self):
        self._beats = None

    # Each subclass returns its name lowercased when coerced to a string
    def __str__(self):
        return self.__class__.__name__.lower()

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

class Paper(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('rock', 'spock')

class Scissors(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('lizard', 'paper')

class Lizard(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('paper', 'spock')

class Spock(Move):
    def __init__(self):
        super().__init__()
        self._beats = ('rock', 'scissors')

class Score:
    def __init__(self):
        self._game_points = 0
        self._total_points = 0
        self._move_history = []
    
    @property
    def points(self):
        return self._game_points
    
    @property
    def total_points(self):
        return self._total_points
    
    @property
    def history(self):
        return tuple(self._move_history)

    def add_point(self):
        self._game_points += 1
        self._total_points += 1

    def add_move(self, move):
        self._move_history.append(str(move))
    
    def reset_points(self):
        self._game_points = 0

class Player:
    CHOICES = (Rock(), Paper(), Scissors(), Lizard(), Spock())

    def __init__(self):
        self.move = None
        self._name = None
        self._score = Score()

    @property
    def score(self):
        return self._score

    @property
    def name(self):
        return self._name

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
        # Add to move history
        for player in (self._human, self._computer):
            player.score.add_move(player.move)

        human_move = self._human.move
        computer_move = self._computer.move

        # Determine winner and add points
        if human_move > computer_move:
            self._human.score.add_point()
            return self._human
        elif computer_move > human_move:
            self._computer.score.add_point()
            return self._computer
        else:
            return None

    def _display_winner(self):
        print(f'You chose: {str(self._human.move).capitalize()}')
        print(f'Computer chose: {str(self._computer.move).capitalize()}')

        winner = self._determine_round_winner()
        if winner == self._human:
            print('You win!')
        elif winner == self._computer:
            print('Computer won. You lost!')
        else:
            print("It's a Tie!")

    def _display_overall_winner(self):
        if self._human.score.points == RPSGame.POINTS_TO_WIN:
            print('You are the overall winner!')
            return True
        elif self._computer.score.points == RPSGame.POINTS_TO_WIN:
            print('Computer is the overall winner!')
            return True
        else:
            return False
    
    def _display_scoreboard(self):
        print(f'{self._human.name} : {self._human.score.points}\n'
              f'{self._computer.name} : {self._computer.score.points}')
        
    def _display_history(self):
        print('Move History:')
        for player in (self._human, self._computer):
            print(player.name)
            print('Total Points:', player.score.total_points)
            print('Moves:')
            for move in player.score.history:
                print('   -', move)
            print()
    
    def _play_again(self):
        prompt = 'Play again? (y/n)'

        while True:
            answer = input(f'{prompt}: ').lower()
            if answer in ('yes', 'no', 'y', 'n'):
                return answer[0] == 'y'

            print('Invalid input. ', end='')

    def _reset(self):
        self._human.score.reset_points()
        self._computer.score.reset_points()

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
                if self._play_again():
                    self._reset()
                else:
                    break

        self._display_goodbye_msg()
        self._display_history()

RPSGame().play()