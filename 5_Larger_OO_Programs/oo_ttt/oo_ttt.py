import pdb
import random
import os
import json

def clear_screen():
    os.system('clear')

class Square:
    EMPTY = ''

    ASCII_MARKS = {
        'x' : (r' \/ ', r' /\ '),
        'o' : (r' /\ ', r' \/ '),
        '' : ('    ', '    ')
    }

    def __init__(self, marker=''):
        self._ascii_mark = None
        self.mark = marker

    def _set_ascii_mark(self, marker):
        self._ascii_mark = Square.ASCII_MARKS[marker]

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, marker):
        self._mark = marker
        self._set_ascii_mark(marker)

    @property
    def ascii_mark(self):
        return self._ascii_mark

    def is_unused(self):
        return self._mark == Square.EMPTY

class Board:
    def __init__(self):
        self._squares = None
        self.reset()

    def count_markers_for(self, player, keys):
        markers = [self._squares[key].mark for key in keys]
        return markers.count(player.marker)

    def display(self):
        print()
        print(f'{self._squares[1].ascii_mark[0]}|'
              f'{self._squares[2].ascii_mark[0]}|'
              f'{self._squares[3].ascii_mark[0]}')
        print(f'{self._squares[1].ascii_mark[1]}|'
              f'{self._squares[2].ascii_mark[1]}|'
              f'{self._squares[3].ascii_mark[1]}')
        print('----+----+----')
        print(f'{self._squares[4].ascii_mark[0]}|'
              f'{self._squares[5].ascii_mark[0]}|'
              f'{self._squares[6].ascii_mark[0]}')
        print(f'{self._squares[4].ascii_mark[1]}|'
              f'{self._squares[5].ascii_mark[1]}|'
              f'{self._squares[6].ascii_mark[1]}')
        print('----+----+----')
        print(f'{self._squares[7].ascii_mark[0]}|'
              f'{self._squares[8].ascii_mark[0]}|'
              f'{self._squares[9].ascii_mark[0]}')
        print(f'{self._squares[7].ascii_mark[1]}|'
              f'{self._squares[8].ascii_mark[1]}|'
              f'{self._squares[9].ascii_mark[1]}')
        print()

    def mark_square_at(self, key, marker):
        self._squares[key].mark = marker

    def unused_squares(self):
        return tuple(key for key, square in self._squares.items()
                     if square.is_unused())

    def is_full(self):
        if len(self.unused_squares()) == 0:
            print('Board is full')
            return True
        return False

    def reset(self):
        self._squares = {
            n : Square() for n in range(1, 10)
        }

class Player:
    def __init__(self, marker):
        self._marker = marker
        self._score = 0

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    @property
    def score(self):
        return self._score

    def add_point(self):
        self._score += 1

class Human(Player):
    HUMAN_MARK = 'x'

    def __init__(self):
        super().__init__(Human.HUMAN_MARK)

class Computer(Player):
    COMPUTER_MARK = 'o'

    def __init__(self):
        super().__init__(Computer.COMPUTER_MARK)

class TTTGame:
    CENTRE_SQ = 5
    WINNING_COMBOS = (
        (1, 2, 3), (4, 5, 6), (7, 8, 9),    # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),    # Columns
        (1, 5, 9), (3, 5, 7)                # Diagonals
    )
    MATCHES_TO_WIN = 3

    def __init__(self):
        self._board = Board()
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_msg(self):
        clear_screen()
        print('Welcome to Tic Tac Toe!')
    
    def _display_rules(self):
        if self._yes_or_no('Do you wish to see the rules?'):
            with open('TTTrules.json', 'r') as file:
                general_rules = json.load(file)['general_rules_msgs']
            
            with open('TTTrules.json', 'r') as file:
                choice_layout = json.load(file)['choice_layout_msgs']

            print()
            for rule in general_rules.values():
                print(rule)
            print()
            self._enter_to_continue()
            print()
            for line in choice_layout.values():
                if isinstance(line, list):
                    print()
                    for nested_line in line:
                        print(nested_line)
                    print() 
                else:
                    print(line)

            print()
            self._enter_to_continue('Hit Enter if you are ready to play...')
            clear_screen()

    def _display_goodbye_msg(self):
        print('Thanks for playing Tic Tac Toe. Goodbye!')

    def _display_results(self):
        if self._is_winner(self._human):
            print('You won! Congratulations!')
        elif self._is_winner(self._computer):
            print('Computer won! You lost.')
        else:
            print('It is a tie!')

    def _display_score(self):
        human_score = self._human.score
        computer_score = self._computer.score

        max_length = len(max(f'Human : {human_score}', 
                             f'Computer : {computer_score}', key=len))
        border = f'+-{'-' * max_length}-+'

        print()
        print(border)
        print(f'| {f'Human : {human_score}'.ljust(max_length, ' ')} |')
        print(f'| {f'Computer : {computer_score}'.ljust(max_length, ' ')} |')
        print(border)
        print()

    @staticmethod
    def _join_or(seq, delim=', ', join_word='or'):
        if len(seq) == 1:
            return str(seq[0])

        end_part = f'{seq[-2]} {join_word} {seq[-1]}'

        if len(seq) > 2:
            start_part = delim.join(str(ele) for ele in seq[:-2]) + delim
            return start_part + end_part

        return end_part

    def _human_moves(self):
        valid_choices = self._board.unused_squares()

        while True:
            choice = input('Choose a square from ('
                           f'{self._join_or(valid_choices)}): ')
            if choice in [str(n) for n in valid_choices]:
                break
            print('Invalid choice. Try again.')

        self._board.mark_square_at(int(choice), Human.HUMAN_MARK)
    
    def _best_move_for(self, player):
        for combo in TTTGame.WINNING_COMBOS:
            if self._n_in_a_row(player, combo, 2):
                for position in combo:
                    if position in self._board.unused_squares():
                        return position
        return None

    def _computer_moves(self):
        unused_sqs = self._board.unused_squares()

        offensive_move = self._best_move_for(self._computer)
        defensive_move = self._best_move_for(self._human)

        if offensive_move:
            choice = offensive_move
        elif defensive_move:
            choice = defensive_move
        elif TTTGame.CENTRE_SQ in unused_sqs:
            choice = TTTGame.CENTRE_SQ
        else:
            choice = random.choice(unused_sqs)

        self._board.mark_square_at(choice, Computer.COMPUTER_MARK)

    def _n_in_a_row(self, player, combo, n):
        return self._board.count_markers_for(player, combo) == n

    def _is_winner(self, player):
        for combo in TTTGame.WINNING_COMBOS:
            if self._n_in_a_row(player, combo, 3):
                return True
        return False

    def _someone_won(self):
        return self._is_winner(self._human) or self._is_winner(self._computer)

    def _game_is_over(self):
        return self._board.is_full() or self._someone_won()

    def _hand_out_points(self):
        if not self._someone_won():
            return

        if self._is_winner(self._human):
            self._human.add_point()
        else:
            self._computer.add_point()

    def _play_again(self):
        if self._yes_or_no('Do you want to play again?'):
            return True
        return False

    @staticmethod
    def _yes_or_no(prompt):
        while True:
            choice = input(f'{prompt} (y/n): ').lower()

            if choice in ('y', 'n', 'yes', 'no'):
                return choice[0] == 'y'

            print('Invalid choice. Try again.')
    
    @staticmethod
    def _enter_to_continue(prompt=None):
        if not prompt:
            input('Press Enter to continue...')
        else:
            input(f'{prompt}')

    def _is_overall_winner(self):
        return self._human.score == 3 or self._computer.score == 3
    
    def _display_overall_winner(self):
        if self._human.score == 3:
            print('You got to 3 points. You won the game!')
        else:
            print('Computer got to 3 points first. You lost the game!')
    
    def _player_turn(self, goes_next):
        if goes_next == self._human:
            self._human_moves()
        else:
            self._computer_moves()
    
    def _toggle_player(self, player):
        if player == self._human:
            return self._computer
        return self._human

    def _play_match(self, first_to_play):
        '''
        Plays a single match of TTT till a winner or tie.
        Adds point to winner.
        '''

        goes_next = first_to_play

        while True:
                self._display_score()
                self._board.display()

                self._player_turn(goes_next)
                if self._game_is_over():
                    break
                
                goes_next = self._toggle_player(goes_next)
                clear_screen()

        self._hand_out_points()

    def play(self):
        starting_player = self._human
        self._display_welcome_msg()
        self._display_rules()

        while True:
            self._play_match(starting_player)

            clear_screen()

            self._display_score()
            self._board.display()
            self._display_results()

            if self._is_overall_winner():
                self._display_overall_winner()
                break

            if not self._play_again():
                break

            goes_first = self._toggle_player(goes_first)
            self._board.reset()
            clear_screen()

        self._display_goodbye_msg()

game = TTTGame()
game.play()

# TODO:
# Display rules, first to 3 etc
# Enter to continues, etc...
# A way for human player to enter thier name?
# A way to choose numpad for choosing moves instead?
# GAme UI improvements, timings etc

# NOTE Human mark and computer mark are defined as constants in Human and
# Computer class respectively