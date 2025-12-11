import random
import time
import os
import json

def clear_screen():
    os.system('clear')

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

class CardAscii:
    with open('TO_card_ascii.json', 'r') as file:
        ASCII_SUITES = json.load(file)

    def __init__(self):
        self._diamond_ascii = CardAscii.ASCII_SUITES['diamonds']
        self._clubs_ascii = CardAscii.ASCII_SUITES['clubs']
        self._hearts_ascii = CardAscii.ASCII_SUITES['hearts']
        self._spades_ascii = CardAscii.ASCII_SUITES['spades']
        self._back_ascii = CardAscii.ASCII_SUITES['back']

    def card_ascii(self, suite=None, rank=None):
        match suite:
            case 'diamonds':
                suite_ascii = self._diamond_ascii
            case 'clubs':
                suite_ascii = self._clubs_ascii
            case 'hearts':
                suite_ascii = self._hearts_ascii
            case 'spades' :
                suite_ascii = self._spades_ascii
            case _:
                suite_ascii = self._back_ascii

        return [self._card_edge()]       + \
               [self._card_top(rank)]    + \
               suite_ascii               + \
               [self._card_bottom(rank)] + \
               [self._card_edge()]

    def _card_top(self, rank=None):
        if rank:
            return f'| {str(rank).ljust(2, ' ')}        |'
        return '| ^  ^^^  ^ |'

    def _card_bottom(self, rank=None):
        if rank:
            return f'|        {str(rank).rjust(2, ' ')} |'
        return '| ^  ^^^  ^ |'

    def _card_edge(self):
        return '+-----------+'

class Card:
    def __init__(self, rank, suite):
        self._rank = rank
        self._suite = suite
        self._ascii_display = CardAscii()

    @property
    def rank(self):
        return self._rank

    def __repr__(self):
        return f'Card({self._rank}, {self._suite})'

    def display(self, hidden=False):
        if not hidden:
            for l in self._ascii_display.card_ascii(self._suite, self._rank):
                print(l)
        else:
            for l in self._ascii_display.card_ascii():
                print(l)

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
        return self.ACE_VALUE

    def hidden_hand_display(self):
        card1, card2 = self._cards[0], self._cards[1]

        card1.display(hidden=True)
        card2.display()

    def hand_display(self):
        for card in self._cards:
            card.display()

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

    def add_card(self, card):
        self._hand.cards.append(card)

    def discard_cards(self):
        self._hand.cards = []

    def display_hand(self):
        self._hand.hand_display()

    def __str__(self):
        return self._name

class Dealer(Participant):
    def __init__(self):
        super().__init__()

    def hit_or_stay(self):
        if self._hand.total >= TOGame.DEALER_STAY_LIMIT:
            return 'stays'
        return 'hits'

    def display_hidden_hand(self):
        return self._hand.hidden_hand_display()

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
            print('Invalid input, please try again.')

    def is_broke(self):
        return self._wallet.amount <= 0

class TOGame:
    TITLE_LENGTH = 80
    HALF_DECK = 26
    STARTING_CASH = 5
    RICH_LIMIT = 10
    BLACKJACK = 21
    DEALER_STAY_LIMIT = 17

    def __init__(self):
        self._dealer = Dealer()
        self._player = Player(TOGame.STARTING_CASH)
        self._deck = Deck()

    @staticmethod
    def _display_welcome_msg():
        with open('TO_ascii_title.json', 'r') as file:
            title_dict = json.load(file)

        print(' Welcome to: '.center(TOGame.TITLE_LENGTH, '*'))
        for line in title_dict["title"]:
            print(line.center(TOGame.TITLE_LENGTH, ' '))
        print()

    @staticmethod
    def _clear_and_display_title():
        clear_screen()
        print(' Twenty One '.center(TOGame.TITLE_LENGTH, '*'))

    @staticmethod
    def _display_goodbye_msg():
        print('Thank you for playing Twenty One! Goodbye.')

    def _display_rules(self):
        if self._yes_or_no('Would you like to see the basic rules?'):
            with open('TO_rules.json', 'r') as file:
                rules_dict = json.load(file)
            print()
            for rule in rules_dict['rules']:
                print(rule)
            print()
        print(f'You will be given ${TOGame.STARTING_CASH} to '
              'begin with.')
        print()

    def _display_player_cash(self):
        cash = self._player.wallet
        if cash < TOGame.STARTING_CASH:
            print(f'You have ${cash} left.')
            print()
        else:
            print(f'You have ${cash} in your wallet.')
            print()

    def _shuffle_cards(self):
        self._check_deck()
        self._deck.shuffle()

    def _deal_cards(self, player1, player2):
        for _ in range(2):
            player1.add_card(self._deck.deal_one())
            player2.add_card(self._deck.deal_one())

    def _check_deck(self):
        deck = self._deck.deck
        if len(deck) < TOGame.HALF_DECK:
            print('Half of deck has already been dealt, shuffling'
                  ' new deck in...')
            self._enter_to_continue()
            self._deck = Deck()
            self._shuffle_cards()

    def _show_cards(self, reveal=False):
        dealer = self._dealer
        player = self._player

        if reveal:
            print('Dealers Hand (Revealed):')
            dealer.display_hand()
            print(f'Dealer Total: {dealer.hand_total}')
        else:
            print('Dealers Hand (Hidden):')
            dealer.display_hidden_hand()
            print(f'Dealer Total: {dealer.hidden_total}')

        print()
        print('Players Hand:')
        player.display_hand()
        print(f'Players Total: {player.hand_total}')
        print()

    def _participants_turn(self, participant):
        title = '* PLAYERS TURN *' if participant == self._player \
            else '* DEALERS TURN *'

        while True:
            self._clear_and_display_title()
            print()
            print(title.center(TOGame.TITLE_LENGTH, ' '))

            if participant == self._dealer:
                self._show_cards(reveal=True)
            else:
                self._show_cards()

            if participant.has_blackjack():
                print(f'{participant} has a natural Blackjack! This is an '
                      'automatic stay.')
                self._enter_to_continue()
                break

            if participant.is_busted():
                print(f'{participant} Busts!')
                self._enter_to_continue()
                break

            if participant.hand_total == TOGame.BLACKJACK:
                print(f"{participant}'s hand total has reached 21. This is "
                      'an automatic stay.')
                self._enter_to_continue()
                break

            choice = participant.hit_or_stay()
            print(f'{participant} {choice}!')
            if choice == 'hits':
                if participant == self._dealer:
                    self._enter_to_continue()
                participant.add_card(self._deck.deal_one())
            else:
                self._enter_to_continue()
                break

    def _place_bet(self):
        bet_max = self._player.wallet
        bet_min = 1

        if bet_max == 1:
            print('Since you only have $1 left, your bet will be set to $1')
            self._player.bet = 1
            self._enter_to_continue('Ready to see the cards? Press Enter to '
                                'continue...')
            return

        while True:
            print(f'Choose between ${bet_min} and ${bet_max} to bet.')
            choice = input('Place bet: $')

            try:
                choice = int(choice)
                if choice not in range(bet_min, bet_max + 1):
                    raise ValueError
            except ValueError:
                print("That's not a valid bet, please try again.")
                continue

            self._player.bet = choice
            break
        print(f'You have placed a ${choice} bet!')
        self._enter_to_continue('Ready to see the cards? Press Enter to '
                                'continue...')

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
        if player.hand_total < dealer.hand_total:
            return dealer
        return 'draw'

    def _determine_and_display_results(self):
        self._clear_and_display_title()
        print()
        print('* RESULTS *'.center(TOGame.TITLE_LENGTH, ' '))

        player = self._player
        dealer = self._dealer

        busted = self._someone_busts()
        if busted:
            other = player if busted == dealer else dealer
            print(f'{busted} has lost the game via a bust! {other} wins!')
            return

        bj_winner = self._someone_has_blackjack()
        match bj_winner:
            case self._player:
                print(f'{self._player} wins with a Natural Blackjack!')
                return
            case self._dealer:
                if self._player.hand_total == TOGame.BLACKJACK:
                    print("It's a draw! Both players have a total of 21.")
                else:
                    print("Dealer wins with a Natural Blackjack!")
                return
            case 'draw':
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
            print('Game ending early because Player is broke!')
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

    def _opening_sequence(self):
        clear_screen()
        self._display_welcome_msg()
        self._display_rules()
        self._enter_to_continue('Ready to start the game?\n'
                                'Press Enter to continue...')

    def _start_game(self):
        self._clear_and_display_title()
        self._display_player_cash()
        self._place_bet()

        self._clear_and_display_title()
        self._shuffle_cards()
        print('Shuffling cards...')
        time.sleep(1)
        self._deal_cards(self._player, self._dealer)
        print('Dealing Cards...')
        time.sleep(1)

    def play(self):
        self._opening_sequence()

        while True:
            self._start_game()

            self._participants_turn(self._player)
            if not self._player.is_busted() and \
                not self._player.has_blackjack():
                self._participants_turn(self._dealer)

            self._determine_and_display_results()
            self._distribute_and_display_winnings(self._get_winner())

            if not self._play_again():
                break

        self._display_player_winnings()
        self._display_goodbye_msg()

game = TOGame()
game.play()

# Any refactoring?
# Final checks
# Reorganise game files