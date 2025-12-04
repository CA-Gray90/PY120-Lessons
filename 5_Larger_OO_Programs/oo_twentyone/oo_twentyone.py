import random

class Deck:
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITES = ['diamonds', 'clubs', 'hearts', 'spades']

    # Maybe returns None if empty? Some way of returning empty. Dealer must
        # instantiate new deck when empty

    def __init__(self):
        self._deck = self._initialize_new_deck()
    
    def _initialize_new_deck(self):
        return [Card(rank, suite) for suite in self.SUITES
                                  for rank in self.RANKS]

    def deal_one(self):
        if self._deck:
            return self._deck.pop()
        return None
    
    def __str__(self):
        return str(self._deck)

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
        self._cards = []
    
    @property
    def cards(self):
        return self._cards

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

    def discard_cards(self):
        # STUB: Discards cards, resets instance variables.
        pass

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

class Player(Participant):
    def __init__(self):
        super().__init__()
        self.wallet = None
    
    @property
    def wallet(self):
        return self._wallet
    
    @wallet.setter
    def wallet(self, amount):
        self._wallet = amount
    
    def hit_or_stay(self):
        while True:
            choice = input('Player chooses either hit or stay: ').lower()
            if choice in {'h', 's', 'hit', 'stay'}:
                return 'hits' if choice[0] == 'h' else 'stays'
            else:
                print('Invalid input, please try again.')

class TOGame:
    DEALER_STAY_LIMIT = 17
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
        self._player = Player()
        self._deck = Deck()

    def _display_welcome_msg(self):
        print('Welcome to Twenty One!')

    def _display_goodbye_msg(self):
        print('Thank you for playing Twenty One! Goodbye.')

    def _shuffle_cards(self):
        self._deck.shuffle()
    
    def _deal_cards(self, player1, player2):
        for _ in range(2):
            player1.add_card(self._deck.deal_one())
            player2.add_card(self._deck.deal_one())

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
        self._participants_turn(self._player)

    def _dealers_turn(self):
        print('Dealers Hand revealed:')
        self._show_cards(reveal=True)
        self._participants_turn(self._dealer)

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

    def play(self):
        self._display_welcome_msg()
        self._shuffle_cards()
        self._deal_cards(self._player, self._dealer)

        self._show_cards()

        self._players_turn()

        if not self._player.is_busted():
            self._dealers_turn()

        self._display_results()
        # self._play_again()
        self._display_goodbye_msg()
    pass

game = TOGame()
game.play()

# Busted outcome doesnt end game yet
# Blackjack should end the game
    # If dealer has (Natural) blackjack from the start, should end the game
        # Player loses
    # If Player has Natural Blackjack: wins

# Dealers turn and players turn very similar, some shared functionality.
# Enter to continues
# displaying cards at better points in the game