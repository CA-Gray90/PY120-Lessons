import random

class Deck:
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITES = ['diamonds', 'clubs', 'hearts', 'spades']

    def __init__(self):
        self._deck = self._initialize_new_deck()
    
    def _initialize_new_deck(self):
        return [Card(rank, suite) for suite in self.SUITES
                                  for rank in self.RANKS]

    @property
    def deck(self):
        return self._deck

    def deal_one(self):
        if self._deck:
            return self._deck.pop()
        return None

    def shuffle(self):
        random.shuffle(self._deck)

class Card:
    def __init__(self, rank, suite):
        self._rank = rank
        self._suite = suite
        self._ascii_display = ''
    
    @property
    def rank(self):
        return self._rank
    
    def __repr__(self):
        return f'Card({self._rank}, {self._suite})'
    
    def hide(self):
        return 'Card is Hidden'

    def display_hidden(self):
        pass

    def display_revealed(self):
        pass

    def _set_display(self):
        pass
    pass

class Hand:
    COURT_CARD_VALUE = 10
    ACE_VALUE = 11

    def __init__(self):
        self.cards = []
    
    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, value):
        self._cards = value

    def _non_ace_card_value(self, card):
        return int(card.rank) if card.rank.isdigit() else self.COURT_CARD_VALUE

    @staticmethod
    def _ace_value(total):
        '''
        Returns 11 or 1 which are the possible values of an Ace.
        '''
        return 1 if total >= 11 else 11

    @property
    def total(self):
        cards = self._cards
        total_value = 0
        aces = 0

        for card in cards:
            if card.rank != 'A':
                total_value += self._non_ace_card_value(card)
            else:
                aces += 1
        
        for _ in range(aces):
            total_value += self._ace_value(total_value)

        return total_value

    @property
    def hidden_total(self):
        card2 = self._cards[1]
        if card2.rank != 'A':
            return self._non_ace_card_value(card2)
        else: 
            return self.ACE_VALUE

    @property
    def hidden_hand(self):
        return str([self._cards[0].hide()] + [self._cards[1]])

    # Currently this is how the hand is displayed:
    def __str__(self):
        return str([self._cards])

class Participant:
    BLACKJACK = 21

    def __init__(self):
        self._hand = Hand()
        self._score = 0         # Overall score; game wins.
        self._name = f'{self.__class__.__name__}'

    @property
    def hand(self):
        return self._hand
    
    @property
    def hand_total(self):
        return self._hand.total
    
    @property
    def name(self):
        return self._name

    def is_busted(self):
        return self._hand.total > Participant.BLACKJACK

    def points(self):
        self._hand.total
    
    def add_card(self, card):
        self._hand.cards.append(card)
    
    def discard_cards(self):
        self._hand.cards = []

class Dealer(Participant):
    STAY_LIMIT = 17

    def __init__(self):
        super().__init__()

    def hit_or_stay(self):
        if self._hand.total >= Dealer.STAY_LIMIT:
            return 'stays'
        else:
            return 'hits'

    # TOGame 'asks' Dealer to show hands, doesn't access hand objects directly
    @property
    def hidden_hand(self):
        return self._hand.hidden_hand

    @property
    def hidden_total(self):
        return self._hand.hidden_total

class Wallet:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount
    
    def deposit(self, amount):
        self._amount += amount
    
    def withdraw(self, amount):
        if self._amount <= 0:
            print('No cash left in wallet!')
        else:
            self._amount -= amount
    
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

class Player(Participant):
    def __init__(self, starting_amount):
        super().__init__()
        self._wallet = Wallet(starting_amount)
    
    @property
    def wallet(self):
        return self._wallet.amount
    
    def add_cash(self, amount):
        self._wallet.deposit(amount)
    
    def remove_cash(self, amount):
        self._wallet.withdraw(amount)
    
    def hit_or_stay(self):
        while True:
            choice = input('Player chooses either hit or stay: ').lower()
            if choice in {'h', 's', 'hit', 'stay'}:
                return 'hits' if choice[0] == 'h' else 'stays'
            else:
                print('Invalid input, please try again.')
    
    def is_broke(self):
        return self._wallet.amount <= 0
class MatchInfo:
    #STUB:
    # Match info object should have information about:
        # Who won, who lost. Method of winning and method of losing
    # Match object can be used for displaying results, distributing winnings
    # Matchinfo object is instantiated by a method that determines a winner

    def __init__(self, winner, win_method, loser, lose_method):
        self._winner = winner
        self._win_method = win_method
        self._loser = loser
        self._lose_method = lose_method
    
    @property
    def winner(self):
        return self._winner
    
    @property
    def winning_method(self):
        return self._win_method
    
    @property
    def loser(self):
        return self._loser
    
    @property
    def losing_method(self):
        return self._lose_method

class TOGame:
    DEALER_STAY_LIMIT = 17
    HALF_DECK = 26
    STARTING_CASH = 5
    RICH_LIMIT = 10
    # STUB:
    # main orchestration function of the game
    # has:
        # Player
        # Dealer
    # Can:
        # Get/display results
        # Start a game with new players
        # Get/display points of players
        # Display winner/loser
        # display overall results of game
        # Give player starting money
        # deduct dollar from player, give player a dollar
    
    # Give option to play game again
    # Kick out player (end program) if broke($0) or rich ($10)

    def __init__(self):
        self._dealer = Dealer()
        self._player = Player(self.STARTING_CASH)
        self._deck = Deck()

    def _display_welcome_msg(self):
        print('Welcome to Twenty One!')
    
    def _display_player_cash(self):
        cash = self._player.wallet
        if cash < self.STARTING_CASH:
            print(f'You have ${cash} left.')
        else:
            print(f'You have ${cash} in your wallet.')

    def _display_goodbye_msg(self):
        print('Thank you for playing Twenty One! Goodbye.')

    def _shuffle_cards(self):
        self._deck.shuffle()
    
    def _deal_cards(self, player1, player2):
        self._check_deck()
        for _ in range(2):
            player1.add_card(self._deck.deal_one())
            player2.add_card(self._deck.deal_one())
    
    def _check_deck(self):
        deck = self._deck.deck
        if len(deck) < self.HALF_DECK:
            print('Half of deck has already been dealt, shuffling'
                  ' new deck in.')
            self._deck = Deck()
            self._shuffle_cards()

    def _show_cards(self, reveal=False):
        dealer = self._dealer
        player = self._player

        if reveal:
            print(f'{dealer.hand} : {dealer.hand_total}')
        else:
            print(f'{dealer.hidden_hand} : {dealer.hidden_total}')
        print(f'{player.hand} : {player.hand_total}')

    def _participants_turn(self, participant):
        while True:
            choice = participant.hit_or_stay()
            print(f'{participant.name} {choice}!')
            if choice == 'hits':
                participant.add_card(self._deck.deal_one())
            else:
                break

            if participant.is_busted():
                print(f'{participant.name} Busts!')
                break

            if participant == self._dealer:
                self._show_cards(reveal=True)
            else:
                self._show_cards()

    def _players_turn(self):
        self._display_player_cash()
        self._participants_turn(self._player)

    def _dealers_turn(self):
        print('Dealers Hand revealed:')
        self._show_cards(reveal=True)
        self._participants_turn(self._dealer)

    def _determine_winner(self):
        pass

    def _display_results(self):
        self._show_cards(self)
        if self._player.is_busted():
            print(f'Player lost game via a Bust! Dealer wins')
        elif self._dealer.is_busted():
            print('Dealer loses via Bust! Player wins the game!')
        elif self._player.hand_total > self._dealer.hand_total:
            print('Player has the higher score. Player wins!')
        elif self._player.hand_total < self._dealer.hand_total:
            print('Dealer has the higher score. Player loses game!')
        else:
            print('Its a draw! No one wins this game.')

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

    def _play_again(self):
        # if self._player.is_broke():
            # skip play again
        # if self._player.is_rich():
            # skip play again

        if self._yes_or_no('Would you like to play again?'):
            self._player.discard_cards()
            self._dealer.discard_cards()
            return True

        return False

    def play(self):
        self._display_welcome_msg()
        self._display_player_cash()
        self._enter_to_continue('Ready to start the game?\n'
                                'Press Enter to continue...')
        while True:
            self._shuffle_cards()
            self._deal_cards(self._player, self._dealer)

            self._show_cards()

            self._players_turn()

            if not self._player.is_busted():
                self._dealers_turn()

            self._display_results()
            if not self._play_again():
                break
        # self._display_player_winnings()
        self._display_goodbye_msg()
    pass

game = TOGame()
game.play()

# Blackjack should end the game
    # If dealer has (Natural) blackjack from the start, should end the game
        # Player loses
    # If Player has Natural Blackjack: wins

# Enter to continues
# Improved UX, UI with clear terminal etc, time delays etc
# displaying cards at better points in the game
# Display simplified rules