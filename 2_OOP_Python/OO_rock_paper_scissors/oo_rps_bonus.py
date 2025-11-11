import random
import os
import json
import time

class Move:
    def __init__(self):
        self._beats = None

    # Each subclass returns its name lowercased when coerced to a string
    def __str__(self):
        return self.__class__.__name__.lower()

    # Each Move subclass knows who it can beat (using comparison operators)
    def __gt__(self, other):
        if not isinstance(other, Move):
            return NotImplemented
        return str(other) in self._beats

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
        self._own_move_history = []
        self._other_move_history = []
    
    @property
    def points(self):
        return self._game_points
    
    @property
    def total_points(self):
        return self._total_points

    @property
    def history(self):
        return tuple(self._own_move_history)

    def add_point(self):
        self._game_points += 1
        self._total_points += 1

    def add_moves(self, move, other_move):
        self._own_move_history.append(str(move))
        self._other_move_history.append(str(other_move))
    
    def reset_points(self):
        self._game_points = 0

class Player:
    CHOICES = {
        'rock' : Rock(),
        'paper' : Paper(),
        'scissors' : Scissors(),
        'lizard' : Lizard(),
        'spock' : Spock()
    }

    CHOICES_ABBREV = {
        'r' : CHOICES['rock'],
        'p' : CHOICES['paper'],
        'sc' : CHOICES['scissors'],
        'l' : CHOICES['lizard'],
        'sp' : CHOICES['spock']
    }

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

    @staticmethod
    def available_choices():
        return [move for move in Player.CHOICES.values()]

class ComputerMixin:
    def choose(self):
        self.move = None

    def speak(self):
        # Each subclass has its own 'personality' or 'speak'?
        pass

    def __str__(self):
        return self._name

class C3PO(ComputerMixin, Player):
    def __init__(self):
        super().__init__()
        self._name = 'C-3PO'
    
    def choose(self):
        self.move = random.choice(self.available_choices())

class R2D2(ComputerMixin, Player):
    def __init__(self):
        super().__init__()
        self._name = 'R2-D2'
        self._preferred_move = Player.CHOICES['rock']

    def choose(self):
        self.move = self._preferred_move

class Hal(ComputerMixin, Player):
    def __init__(self):
        super().__init__()
        self._name = 'HAL 9000'
        self._preferred_move = Player.CHOICES['scissors']
    
    def choose(self):
        while True:
            random_choice = random.choice(self.available_choices())
            if random_choice != self._preferred_move:
                break

        self.move = random.choice((self._preferred_move, random_choice))

class Daneel(ComputerMixin, Player):
    def __init__(self):
        super().__init__()
        self._name = 'R. Daneel Olivaw'
    
    def choose(self):
        if len(self.score._other_move_history) >= 1:
            self.move = Player.CHOICES[self.score._other_move_history[-1]]
        else:
            self.move = random.choice(self.available_choices())
        # print(f'move history of daneel:')
        # print(self.score.__dict__)

class PromptMixin:
    @staticmethod
    def _prompt(text):
        return f'> {text}'

class Human(PromptMixin, Player):
    def __init__(self):
        super().__init__()
        self._name = 'Human Player'

    def choose(self):
        prompt = self._prompt("Enter either '(r)ock', '(p)aper', '(sc)issors', "
                  "'(l)izard' or '(sp)ock'")

        while True:
            choice = input(f'{prompt}: ').lower()

            if choice in Player.CHOICES_ABBREV.keys():
                self.move = Player.CHOICES_ABBREV[choice]
                break
            elif choice in Player.CHOICES.keys():
                self.move = Player.CHOICES[choice]
                break

            print('Invalid input.')

class RPSGame(PromptMixin):
    POINTS_TO_WIN = 5
    DISPLAY_LENGTH = 80
    GAME_TITLE = 'Rock, Paper, Scissors, Lizard, Spock!'

    def __init__(self):
        self._human = Human()
        self._computer = Daneel()

    # @staticmethod
    # def _prompt(text):
    #     return f'> {text}'

    def _enter_to_continue(self):
        input(f'{self._prompt('Enter to continue...')}')
    
    def _display_game_title(self):
        print(f'{f' {RPSGame.GAME_TITLE} '.center(RPSGame.DISPLAY_LENGTH, '*')}')
        print()

    def _display_welcome_msg(self):
        print(f'{f' Welcome to {RPSGame.GAME_TITLE} '.center(RPSGame.DISPLAY_LENGTH, '*')}')
        print(f'{f'First to {RPSGame.POINTS_TO_WIN} wins!'.center(RPSGame.DISPLAY_LENGTH, ' ')}')
        print()

    def _display_ruleset(self):
        if self._prompt_user('Would you like to see the rules? (y/n)'):
            print()
            with open('RPSrules.json', 'r') as file:
                ruleset = json.load(file)

            for line in ruleset:
                print(''.join(ruleset[line]))
                print()
                self._enter_to_continue()
            print()
            print(f'Remember: First to {RPSGame.POINTS_TO_WIN} wins!')
        print()
    
    def _display_game_countdown(self):
        print('Game will start in...')
        for num in range(3, 0, -1):
            print(f'{num}...')
            time.sleep(1)

        print('Game Start!')
        time.sleep(1)

    def _display_match_countdown(self):
        pass

    def _display_goodbye_msg(self):
        print('Thanks for playing. Goodbye!')

    def _add_to_history(self):
        human_move = self._human.move
        computer_move = self._computer.move

        self._human.score.add_moves(human_move, computer_move)
        self._computer.score.add_moves(computer_move, human_move)

    def _determine_round_winner(self):
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
        print(f'{self._computer} chose: {str(self._computer.move).capitalize()}')

        winner = self._determine_round_winner()
        if winner == self._human:
            print('You win!')
        elif winner == self._computer:
            print(f'{self._computer} won. You lost!')
        else:
            print("It's a Tie!")

    def _display_overall_winner(self):
        if self._human.score.points == RPSGame.POINTS_TO_WIN:
            print('You are the overall winner!')
            return True
        elif self._computer.score.points == RPSGame.POINTS_TO_WIN:
            print(f'{self._computer} is the overall winner!')
            return True
        else:
            return False
    
    def _display_scoreboard(self):
        print(f'{self._human.name} : {self._human.score.points}\n'
              f'{self._computer} : {self._computer.score.points}')
        
    def _display_history(self):
        print('Move History:')
        for player in (self._human, self._computer):
            print(player.name)
            print('Total Points:', player.score.total_points)
            print('Moves:')
            for move in player.score.history:
                print('   -', move)
            print()

    def _prompt_user(self, question):
        while True:
            answer = input(f'{self._prompt(question)}: ').lower()
            if answer in ('yes', 'no', 'y', 'n'):
                return answer[0] == 'y'

            print('Invalid input.')

    def _reset(self):
        self._human.score.reset_points()
        self._computer.score.reset_points()
    
    def _program_start(self):
        os.system('clear')
        self._display_welcome_msg()
        self._display_ruleset()
        print('Ready to play?')
        self._enter_to_continue()

    def _set_up_game(self):
        self._reset()
        os.system('clear')
        self._display_game_title()
        self._display_game_countdown()

    def _play_round(self):
        os.system('clear')
        self._display_game_title()
        self._human.choose()
        self._computer.choose()
        self._display_winner()
        self._add_to_history()
        self._display_scoreboard()

    # Orchestration function to play the game
    def play(self):
        self._program_start()
        keep_playing = True

        while keep_playing:
            self._set_up_game()

            while True:
                self._play_round()
                if not self._display_overall_winner():
                    print('Ready for the next round?')
                    self._enter_to_continue()

                elif self._prompt_user('Play again? (y/n)'):
                    break

                else:
                    keep_playing = False
                    break

        self._display_goodbye_msg()
        self._display_history()

RPSGame().play()

#Todo
# Change CHOICES dict to tuples for keys?
# Personalities? Or speak methods for computer players?
# upgrade Daneel choices to pick statistically likely moves...?
# Friendly UI, clear terminal, rules, countdowns... game pauses etc etc.
# prompt display for everytime a user needs to input something