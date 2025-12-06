import pdb
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
        return self._hand.total > TOGame.BLACKJACK
    
    def has_blackjack(self):
        # Has 21 with two cards
        return self._hand.total == TOGame.BLACKJACK and \
        len(self._hand.cards) == 2

    def points(self):
        self._hand.total
    
    def add_card(self, card):
        self._hand.cards.append(card)
    
    def discard_cards(self):
        self._hand.cards = []
    
    def __str__(self):
        return self._name

class Dealer(Participant):
    def __init__(self):
        super().__init__()

    def hit_or_stay(self):
        if self._hand.total >= TOGame.DEALER_STAY_LIMIT:
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
        self._bet = 0
    
    @property
    def wallet(self):
        return self._wallet.amount
    
    @property
    def bet(self):
        return self._bet
    
    @bet.setter
    def bet(self, value):
        self._bet = value

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

class TOGame:
    HALF_DECK = 26
    STARTING_CASH = 5
    RICH_LIMIT = 10
    # BET = 1
    BLACKJACK = 21
    DEALER_STAY_LIMIT = 17

    def __init__(self):
        self._dealer = Dealer()
        self._player = Player(TOGame.STARTING_CASH)
        self._deck = Deck()

    def _display_welcome_msg(self):
        print('Welcome to Twenty One!')
    
    def _display_player_cash(self):
        cash = self._player.wallet
        if cash < TOGame.STARTING_CASH:
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
        if len(deck) < TOGame.HALF_DECK:
            print('Half of deck has already been dealt, shuffling'
                  ' new deck in.')
            self._deck = Deck()
            self._shuffle_cards()

    def _show_cards(self, reveal=False):
        dealer = self._dealer
        player = self._player

        if reveal:
            print(f'Dealers Hand:\n{dealer.hand} : {dealer.hand_total}')
        else:
            print(f'Dealers Hand:\n{dealer.hidden_hand} : {dealer.hidden_total}')
        print(f'Players Hand:\n{player.hand} : {player.hand_total}')

    def _participants_turn(self, participant):
        while True:
            if participant.hand_total == TOGame.BLACKJACK:
                print(f"{participant}'s hand total has reached 21. This is "
                      'an automatic stay.')
                break

            choice = participant.hit_or_stay()
            print(f'{participant} {choice}!')
            if choice == 'hits':
                participant.add_card(self._deck.deal_one())
            else:
                break

            if participant.is_busted():
                print(f'{participant} Busts!')
                break

            if participant == self._dealer:
                self._show_cards(reveal=True)
            else:
                self._show_cards()
    
    def _place_bet(self):
        bet_max = self._player.wallet
        bet_min = 1

        if bet_max == 1:
            print('Since you only have $1 left, your bet will be set to $1')
            self._player.bet = 1
            return

        print('How much would you like to bet?')
        while True:
            print(f'Choose between ${bet_min} and ${bet_max}')
            choice = input('Place bet: ')

            try:
                choice = int(choice)
                if choice not in range(bet_min, bet_max + 1):
                    raise ValueError
            except ValueError:
                print("That's not a valid bet, please try again.")

            self._player.bet = choice
            break

    def _players_turn(self):
        if not self._player.has_blackjack():
            self._participants_turn(self._player)
        else:
            print('Player has a natural Blackjack! This is an automatic stay.')

    def _dealers_turn(self):
        print('Dealers Hand revealed:')
        self._show_cards(reveal=True)
        self._participants_turn(self._dealer)

    def _someone_busts(self):
        for player in (self._player, self._dealer):
            if player.is_busted():
                return player
        return None

    def _someone_has_blackjack(self):
        if self._player.has_blackjack() and self._dealer.has_blackjack():
            return 'draw'

        for player in (self._player, self._dealer):
            if player.has_blackjack():
                return player
        return None
    
    def _win_by_totals(self):
        player = self._player
        dealer = self._dealer

        if player.hand_total > dealer.hand_total:
            return player
        elif player.hand_total < dealer.hand_total:
            return dealer
        else:
            return 'draw'

    def _determine_and_display_results(self):
        player = self._player
        dealer = self._dealer

        self._show_cards(self)

        busted = self._someone_busts()
        if busted:
            other = player if busted == dealer else dealer
            print(f'{busted} has lost the game via a bust! {other} wins!')
            return

        bj_winner = self._someone_has_blackjack()
        if bj_winner:
            if bj_winner != 'draw':
                print(f'{bj_winner} wins with a Natural Blackjack!')
            else:
                print("It's a draw! Both players had a Blackjack.")
            return

        totals_winner = self._win_by_totals()
        if totals_winner != 'draw':
            other = player if totals_winner == dealer else dealer
            print(f'{totals_winner} won via a higher total! {other} loses '
                  'this hand.')
        else:
            print("It's a draw! No one wins this hand")

    def _get_winner(self):
        player = self._player
        dealer = self._dealer
        
        if player.is_busted():
            return dealer
        if dealer.is_busted():
            return player
        
        bj_winner = self._someone_has_blackjack()
        if bj_winner:
            return bj_winner
        
        return self._win_by_totals()

    def _distribute_and_display_winnings(self, winner):
        bet = self._player.bet
        match winner:
            case self._player:
                self._player.add_cash(bet)
                print(f'{self._player} wins ${bet}!')
            case self._dealer:
                self._player.remove_cash(bet)
                print(f'{self._player} loses ${bet}.')
            case 'draw':
                print(
                    'A draw results in no winnings being distributed.'
                    )
        self._display_player_cash()

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

    @staticmethod
    def _too_rich(player):
        return player.wallet >= TOGame.RICH_LIMIT

    def _play_again(self):
        if self._player.is_broke():
            return False
        if self._too_rich(self._player):
            return False

        if self._yes_or_no('Would you like to play again?'):
            self._player.discard_cards()
            self._dealer.discard_cards()
            return True

        return False

    def _display_player_winnings(self):
        difference = abs(TOGame.STARTING_CASH - self._player.wallet)
        if self._player.is_broke():
            print('Game ending early because Player is broke!\n' \
            'You lost all your cash...')
        elif self._player.wallet < TOGame.STARTING_CASH:
            print(
                f"You've finished the game with ${self._player.wallet} left.\n"
                f"You lost ${difference} overall."
                )
        elif self._player.wallet == TOGame.STARTING_CASH:
            print('You finished with the same amount of cash that you started '
                  'with.')
        elif self._player.wallet >= TOGame.RICH_LIMIT:
            print("You've reached the limit for what this casino is willing "
                  "to pay out.\nYou've been kicked out!")
            print(f"You've finished with ${self._player.wallet} in the wallet "
                  f"and ${difference} in profit!")
        elif self._player.wallet > TOGame.STARTING_CASH:
            print(f"Congratulations, you've finished with "
                  f"${self._player.wallet}!")
            print(f"You made ${difference} profit!")

    def play(self):
        self._display_welcome_msg()
        self._display_player_cash()
        self._enter_to_continue('Ready to start the game?\n'
                                'Press Enter to continue...')
        while True:
            self._shuffle_cards()
            self._deal_cards(self._player, self._dealer)
            self._display_player_cash()
            self._place_bet()
            self._show_cards()

            self._players_turn()
            if not self._player.is_busted() and \
                not self._player.has_blackjack():
                self._dealers_turn()

            self._determine_and_display_results()
            self._distribute_and_display_winnings(self._get_winner())
            if not self._play_again():
                break
        self._display_player_winnings()
        self._display_goodbye_msg()
    pass

game = TOGame()
game.play()

# Enter to continues
# Improved UX, UI with clear terminal etc, time delays etc
# displaying cards at better points in the game
# Display simplified rules
# Player able to place bet?