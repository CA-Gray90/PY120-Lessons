import random

class Square:
    EMPTY = ('    ', '    ')
    X_MARK = (r' \/ ', r' /\ ')
    O_MARK = (r' /\ ', r' \/ ')

    def __init__(self, marker=None):
        self.mark = marker
    
    @property
    def mark(self):
        return self._mark
    
    @mark.setter
    def mark(self, marker):
        match marker:
            case 'x':
                self._mark = Square.X_MARK
            case 'o':
                self._mark = Square.O_MARK
            case None:
                self._mark = Square.EMPTY
    
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
    def display(self):
        print()
        print(f'{self._squares[1].mark[0]}|{self._squares[2].mark[0]}|{self._squares[3].mark[0]}')
        print(f'{self._squares[1].mark[1]}|{self._squares[2].mark[1]}|{self._squares[3].mark[1]}')
        print(f'----+----+----')
        print(f'{self._squares[4].mark[0]}|{self._squares[5].mark[0]}|{self._squares[6].mark[0]}')
        print(f'{self._squares[4].mark[1]}|{self._squares[5].mark[1]}|{self._squares[6].mark[1]}')
        print(f'----+----+----')
        print(f'{self._squares[7].mark[0]}|{self._squares[8].mark[0]}|{self._squares[9].mark[0]}')
        print(f'{self._squares[7].mark[1]}|{self._squares[8].mark[1]}|{self._squares[9].mark[1]}')
        print()

    def mark_square_at(self, key, marker):
        self._squares[key].mark = marker

    def unused_squares(self):
        return tuple(key for key, square in self._squares.items()
                     if square.is_unused())

class Row:
    def __init__(self):
        pass
    # STUB:
    # Need a way to identify 3 squares in a row, what a row is

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

    def mark(self):
        # A way to mark the board. 
        # Both players have a particular mark
        pass

class Human(Player):
    HUMAN_MARK = 'x'

    def __init__(self):
        super().__init__(Human.HUMAN_MARK)
        pass

    # STUB:
    # Human player can make choice of square to mark

class Computer(Player):
    COMPUTER_MARK = 'o'
    def __init__(self):
        super().__init__(Computer.COMPUTER_MARK)
        pass

    # STUB:
    # Computer player makes choices automatically, depending on different
    # difficulty/strategy?

class TTTGame:
    def __init__(self):
        # STUBS:
        # Need a board and two players
        self._board = Board()
        self._human = Human()
        self._computer = Computer()
        pass
        
    def _display_welcome_msg(self):
        print('Welcome to Tic Tac Toe!')

    def _display_goodbye_msg(self):
        print('Thanks for playing Tic Tac Toe. Goodbye!')

    def _display_results(self):
        pass

    def _human_moves(self):
        valid_choices = self._board.unused_squares()

        while True:
            choice = input(f'Choose a square {valid_choices}: ')
            # Better way to display choices left? 1, 2, or 3 for example
            if choice in [str(n) for n in valid_choices]:
                break
            else:
                print('Invalid choice. Try again.')

        self._board.mark_square_at(int(choice), Human.HUMAN_MARK)

    def _computer_moves(self):
        choice = random.choice(self._board.unused_squares())
        self._board.mark_square_at(choice, Computer.COMPUTER_MARK)

    def _game_is_over(self):
        return False

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

        # self._board.display()
        self._display_results()
        self._display_goodbye_msg()
    
game = TTTGame()
game.play()

# TODO:
# Moves can currently overwrite each other.
# Game currently loops indefinitely, there is no break condition yet
# NOTE Human mark and computer mark are defined as constants in Human and Computer class respectively