class Square:
    def __init__(self):
        pass
    # STUB
    # Does the square keep track of its marker?

class Board:
    def __init__(self):
        pass
    # STUB
    # Board has squares? 
    # Rows, columns?
    # Keeps track of all the marks
    # Is it able to determine a winner, tie, etc?
    # A way to display itself to the terminal?

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
        # STUB:
        # Main orchestration engine of the game
        # Need a board and two players
        pass

    def play(self):
        # Sets off the game. Main orchestration of the game

        # Spike:
        '''
        - Displays welcome message
        - Rules?
        > Repeat until game is over:
            - Display current state of board
            - 1st Player marks a square
            - If there is a winner: Exit the loop
            - 2nd Player makrs a square
            - If there is a winner: Exit the loop
            
        - Display current state of board
        - Declare winner, display final result
        - Exit Game
        '''

        self._display_welcome_msg()

        while True:
            self._display_board()

            self._first_player_move()
            if self._game_is_over():
                break

            self._second_player_move()
            if self._game_is_over():
                break

            break # Loop executes only once for now

        self._display_board()
        self._display_results()
        self._display_goodbye_msg()
        
    def _display_welcome_msg(self):
        print('Welcome to Tic Tac Toe!')

    def _display_goodbye_msg(self):
        print('Thanks for playing Tic Tac Toe. Goodbye!')

    def _display_results(self):
        pass

    def _display_board(self):
        pass

    def _first_player_move(self):
        pass

    def _second_player_move(self):
        pass

    def _game_is_over(self):
        return False
    
game = TTTGame()
game.play()