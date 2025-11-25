class Square:
    EMPTY = ('    ', '    ')
    X_MARK = (r' \/ ', r' /\ ')
    O_MARK = (r' /\ ', r' \/ ')

    def __init__(self, marker=None):
        match marker:
            case 'x':
                self._mark = Square.X_MARK
            case 'o':
                self._mark = Square.O_MARK
            case None:
                self._mark = Square.EMPTY
    
    @property
    def mark(self):
        return self._mark

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
        print(f'{self._squares[1].mark[1]}|{self._squares[2].mark[1]}|{self._squares[3].mark[0]}')
        print(f'----+----+----')
        print(f'{self._squares[4].mark[0]}|{self._squares[5].mark[0]}|{self._squares[6].mark[0]}')
        print(f'{self._squares[4].mark[1]}|{self._squares[5].mark[1]}|{self._squares[6].mark[1]}')
        print(f'----+----+----')
        print(f'{self._squares[7].mark[0]}|{self._squares[8].mark[0]}|{self._squares[9].mark[0]}')
        print(f'{self._squares[7].mark[1]}|{self._squares[8].mark[1]}|{self._squares[9].mark[1]}')
        print()

class Row:
    def __init__(self):
        pass
    # STUB:
    # Need a way to identify 3 squares in a row, what a row is

class Marker:
    def __init__(self):
        pass
    # STUB:
    # A mark object, either X or O.
    # IDentifies as belonging to either player

class Player:
    def __init__(self):
        pass

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

    def play(self):
        pass

class Human(Player):
    def __init__(self):
        super().__init__()
        pass

    # STUB:
    # Human player can make choice of square to mark

class Computer(Player):
    def __init__(self):
        super().__init__()
        pass

    # STUB:
    # Computer player makes choices automatically, depending on different
    # difficulty/strategy?

class TTTGame:
    def __init__(self):
        # STUBS:
        # Main orchestration engine of the game
        # Need a board and two players
        self._board = Board()
        pass
        
    def _display_welcome_msg(self):
        print('Welcome to Tic Tac Toe!')

    def _display_goodbye_msg(self):
        print('Thanks for playing Tic Tac Toe. Goodbye!')

    def _display_results(self):
        pass

    def _first_player_move(self):
        pass

    def _second_player_move(self):
        pass

    def _game_is_over(self):
        return False

    def play(self):
        # Sets off the game. Main orchestration of the game
        self._display_welcome_msg()

        while True:
            self._board.display()

            self._first_player_move()
            if self._game_is_over():
                break

            self._second_player_move()
            if self._game_is_over():
                break

            break # Loop executes only once for now

        self._board.display()
        self._display_results()
        self._display_goodbye_msg()
    
game = TTTGame()
game.play()