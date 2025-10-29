import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self, player_type):
        self._player_type = player_type.lower()
        self.move = None

    def _is_human(self):
        return self._player_type == 'human'

    def choose(self):
        if self._is_human():
            prompt = "Enter either 'rock', 'paper' or 'scissors'"

            while True:
                move = input(f'{prompt}: ').lower()
                if move in Player.CHOICES:
                    break

                else: print('Invalid input. ', end='')
            
            self.move = move

        else:
            self.move = random.choice(Player.CHOICES)

class Move:
    def __init__(self):
        pass
    # contains move choices?
    pass

    # def compare here?

class Rules:
    def __init__(self):
        pass
    # Game rules defining who wins by comparing moves
    pass

    # def compare here?

class RPSGame:
    def __init__(self):
        self._human = Player('human') # collaborator objects
        self._computer = Player('computer')

    def _display_welcome_msg(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_msg(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _display_winner(self):
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'You chose: {human_move.capitalize()}')
        print(f'Computer chose: {computer_move.capitalize()}')

        if ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper')):
            print('You win!')
        
        elif ((human_move == 'rock' and computer_move == 'paper') or \
              (human_move == 'paper' and computer_move == 'scissors') or \
              (human_move == 'scissors' and computer_move == 'rock')):
            print('Computer won. You lost!')

        else:
            print("It's a Tie!")
    
    def _play_again(self):
        prompt = 'Play again? (y/n)'

        while True:
            answer = input(f'{prompt}: ').lower()
            if answer in ('yes', 'no', 'y', 'n'):
                return answer[0] == 'y'
            
            else: print('Invalid input. ', end='') 

    def play(self):
        self._display_welcome_msg()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break

        self._display_goodbye_msg()

game = RPSGame().play()