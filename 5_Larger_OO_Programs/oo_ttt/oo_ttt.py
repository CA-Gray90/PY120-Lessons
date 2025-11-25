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

class Row:
    def __init__(self):
        pass
    # STUB:
    # Need a way to identify 3 squares in a row, what a row is

class Marker:
    HUMAN_MARK = 'x'
    COMPUTER_MARK = 'o'
    # Maybe we can set these later

    def __init__(self):
        pass
    # STUB:
    # A mark object, either X or O.
    # IDentifies as belonging to either player

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

    def play(self):
        pass

class Human(Player):
    def __init__(self):
        super().__init__(Marker.HUMAN_MARK)
        pass

    # STUB:
    # Human player can make choice of square to mark

class Computer(Player):
    def __init__(self):
        super().__init__(Marker.COMPUTER_MARK)
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
        while True:
            choice = input('Choose between 1 and 9: ')
            if choice in [str(n) for n in range(1, 10)]:
                break
            else:
                print('Invalid choice. Try again.')

        self._board.mark_square_at(int(choice), 'x')

    def _computer_moves(self):
        print('Computer moves')

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

            self._board.display()

            self._computer_moves()
            if self._game_is_over():
                break

            break # Loop executes only once for now

        # self._board.display()
        self._display_results()
        self._display_goodbye_msg()
    
game = TTTGame()
game.play()