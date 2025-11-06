import random
import os

class Move:
    def __str__(self):
        return self.__class__.__name__

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        return str(other) == str(self)

class Rock(Move):
    def __gt__(self, other):
        return str(other) in ('Lizard', 'Scissors')

class Paper(Move):
    def __gt__(self, other):
        return str(other) in ('Rock', 'Spock')

class Scissors(Move):
    def __gt__(self, other):
        return str(other) in ('Paper', 'Lizard')

class Lizard(Move):
    def __gt__(self, other):
        return str(other) in ('Spock', 'Paper')

class Spock(Move):
    def __gt__(self, other):
        return str(other) in ('Scissors', 'Rock')

class Player:
    CHOICE_TO_CLASS = { 'rock': Rock,
                        'paper': Paper,
                        'scissors': Scissors,
                        'lizard': Lizard,
                        'spock': Spock }
    CHOICES = list(CHOICE_TO_CLASS.keys())

    def __init__(self):
        self.move = None
        self.score = 0
        self.moves = []

    def reset_score(self):
        self.score = 0
        self.moves = []

    # also handles adding the current `move` to `moves`
    def _set_move(self, choice):
        self.move = Player.CHOICE_TO_CLASS[choice]()
        self.moves.append(self.move)

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        choice = random.choice(Player.CHOICES)
        self._set_move(choice)

class R2D2(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self._set_move('rock')

class HAL(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        weighted_choices = list(Player.CHOICES) + ['scissors']
        choice = random.choice(weighted_choices)
        self._set_move(choice)

class Daneel(Player):
    def __init__(self):
        super().__init__()

    def choose(self, player):
        if len(player.moves) == 1:
            choice = random.choice(Player.CHOICES)
        else:
            choice = str(player.moves[-2]).lower()
        self._set_move(choice)

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = 'Please choose rock(r), paper(p), scissors(sc), ' \
                    'lizard(l), or spock(sp): '
        choice_abbrevations = ['r', 'p', 'sc', 'l', 'sp']
        abbrevations_to_move = dict(zip(choice_abbrevations, Player.CHOICES))
        while True:
            choice = input(prompt).lower()
            if not choice:
                print('You have to make a choice.', end=" ")
                continue
            found_move = None
            for abbrevation in choice_abbrevations:
                if choice.lower().startswith(abbrevation):
                    found_move = abbrevations_to_move[abbrevation]
                    break
            if found_move:
                self._set_move(found_move)
                break
            print(f'Sorry, {choice} is not valid.', end=" ")

class RPSGame:
    OPPONENT_TO_CLASS = {'computer': Computer,
                         'r2d2': R2D2,
                         'hal': HAL,
                         'daneel': Daneel}
    OPPONENTS = list(OPPONENT_TO_CLASS.keys())

    def __init__(self):
        self._human = Human()
        self._opponent = None

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors Lizard Spock!')
        print('First to 5 wins!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!')

    def _human_wins(self):
        human_move = self._human.move
        opponent_move = self._opponent.move
        return human_move > opponent_move

    def _opponent_wins(self):
        human_move = self._human.move
        opponent_move = self._opponent.move
        return opponent_move > human_move

    def _display_round_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'Your opponent chose: {self._opponent.move}')

        if self._human_wins():
            print('You win this round!')
            self._human.score += 1
        elif self._opponent_wins():
            print('Your opponent wins this round!')
            self._opponent.score += 1
        else:
            print("It's a tie")

    def _display_round_score(self):
        print(f'Human score: {self._human.score}')
        print(f'Opponent score: {self._opponent.score}')

    def _opponent_reaches_game(self):
        return self._opponent.score == 5

    def _human_reaches_game(self):
        return self._human.score == 5

    def _display_game_winner(self):
        if self._human_reaches_game():
            print('You win the game!')
        if self._opponent_reaches_game():
            print('Opponent wins the game!')

    def _reset_player_score(self):
        self._human.reset_score()
        self._opponent.reset_score()

    def _display_history(self):
        player_move_list = [str(move) for move in self._human.moves]
        opponent_move_list = [str(move) for move in self._opponent.moves]
        player_move_string = ', '.join(player_move_list)
        opponent_move_string = ', '.join(opponent_move_list)
        print('Your Move History: ', player_move_string)
        print('Opponent\'s Move History: ', opponent_move_string)

    def _delay_prompt(self):
        input("Press enter to continue...")
        os.system('clear')

    def _set_opponent(self):
        prompt = "Who would you like to play against? " \
                 "(Computer, R2D2, HAL, Daneel): "
        while True:
            opponent = input(prompt)
            if opponent.lower() in RPSGame.OPPONENTS:
                self._opponent = RPSGame.OPPONENT_TO_CLASS[opponent.lower()]()
                break
            print(f'Your choice, {opponent} is invalid. Try again.')

    def _opponent_choose(self):
        if isinstance(self._opponent, Daneel):
            self._opponent.choose(self._human)
        else:
            self._opponent.choose()

    def play(self):
        self._display_welcome_message()
        while True:
            self._set_opponent()

            while True:
                self._human.choose()
                self._opponent_choose()
                self._display_round_winner()
                self._display_round_score()

                if (self._opponent_reaches_game() or
                       self._human_reaches_game()):
                    break

                self._delay_prompt()

            self._display_game_winner()
            self._display_history()
            self._reset_player_score()
            if not self._play_again():
                break

        self._display_goodbye_message()

    def _play_again(self):
        while True:
            answer = input('Would you like to play again? (y/n): ')
            if not answer:
                print('Your have to make a choice.', end=' ')
                continue
            if answer[0].lower().startswith('n'):
                return False
            if answer[0].lower().startswith('y'):
                return True
            print(f'Your choice, {answer}, is invalid. Try again.', end=' ')


RPSGame().play()