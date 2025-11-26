import pdb
import random
import os

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

    # STUB
    # Does the square keep track of its marker?

class Board:
    def __init__(self):
        self._squares = {
            n : Square() for n in range(1, 10)
        }

    # STUB
    # Board has squares?
    # Rows, columns?
    # Keeps track of all the marks
    # Is it able to determine a winner, tie, etc?
    # A way to display itself to the terminal?

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

class Player:
    def __init__(self, marker):
        self._marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    # STUB:
    # Players can be either computer or human
    # Human player can choose square to mark
    # computer choose automatically, perhaps has a difficulty level, etc
    # Players can 'mark' a square
    # Players have a score?

class Human(Player):
    HUMAN_MARK = 'x'

    def __init__(self):
        super().__init__(Human.HUMAN_MARK)

    # STUB:
    # Human player can make choice of square to mark

class Computer(Player):
    COMPUTER_MARK = 'o'
    def __init__(self):
        super().__init__(Computer.COMPUTER_MARK)

    # STUB:
    # Computer player makes choices automatically, depending on different
    # difficulty/strategy?

class TTTGame:
    WINNING_COMBOS = (
        (1, 2, 3), (4, 5, 6), (7, 8, 9),    # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),    # Columns
        (1, 5, 9), (3, 5, 7)                # Diagonals
    )

    def __init__(self):
        # STUBS:
        # Need a board and two players
        self._board = Board()
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_msg(self):
        clear_screen()
        print('Welcome to Tic Tac Toe!')

    def _display_goodbye_msg(self):
        print('Thanks for playing Tic Tac Toe. Goodbye!')

    def _is_winner(self, player):
        for combo in TTTGame.WINNING_COMBOS:
            if self._three_in_a_row(player, combo):
                return True
        return False

    def _display_results(self):
        if self._is_winner(self._human):
            print('You won! Congratulations!')
        elif self._is_winner(self._computer):
            print('Computer won! You lost.')
        else:
            print('It is a tie!')

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

    def _computer_moves(self):
        choice = random.choice(self._board.unused_squares())
        self._board.mark_square_at(choice, Computer.COMPUTER_MARK)

    def _game_is_over(self):
        return self._board.is_full() or self._someone_won()

    def _three_in_a_row(self, player, combo):
        return self._board.count_markers_for(player, combo) == 3

    def _someone_won(self):
        return self._is_winner(self._human) or self._is_winner(self._computer)

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

    def play(self):
        # Sets off the game. Main orchestration of the game
        self._display_welcome_msg()

        while True:
            self._board.display()

            self._human_moves()
            if self._game_is_over():
                break

            # self._board.display()

            self._computer_moves()
            if self._game_is_over():
                break

            # Currently loops indefinitly
            clear_screen()

        clear_screen()
        self._board.display()
        self._display_results()
        self._display_goodbye_msg()

game = TTTGame()
game.play()

# TODO:
# Display for choices for player could be cleaned up: 1, 2, or 4 (for example)
# Still may be some confusion around marks 'x' and 'o'. Perhaps Markers does
# need to be a class as a Mixin?
# Game currently loops indefinitely, raises error when we get to a full board
# NOTE Human mark and computer mark are defined as constants in Human and
# Computer class respectively