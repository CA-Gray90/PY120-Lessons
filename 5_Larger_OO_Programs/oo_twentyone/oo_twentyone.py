import random

class Deck:
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITES = ['diamonds', 'clubs', 'hearts', 'spades']
    # STUB:
    # Has 52 cards (another class?)
        # A dictionary of card objects?
    # Can shuffle?
    # Maybe returns None if empty? Some way of returning empty. Dealer must
        # instantiate new deck when empty

    def __init__(self):
        self._deck = self._initialize_new_deck()
    
    def _initialize_new_deck(self):
        return [Card(rank, suite) for suite in self.SUITES
                                  for rank in self.RANKS]

    def deal(self):
        return self._deck.pop()
    
    def __str__(self):
        return str(self._deck)

    def shuffle(self):
        random.shuffle(self._deck)

    pass

class Card:
    # STUB:
    # has rank and suite
    # knows how to display visually
        # knows how to hide
    # has value (rank)
    # knows how to add?
    # how does Aces work...?

    def __init__(self, rank, suite):
        self._rank = rank
        self._suite = suite
        self._ascii_display = ''
    
    @property
    def rank(self):
        return self._rank
    
    def __repr__(self):
        return f'Card({self._rank}, {self._suite})'

    def display_hidden(self):
        pass

    def display_revealed(self):
        pass

    def _set_display(self):
        pass
    pass

class Hand:
    COURT_CARD_VALUE = 10

    def __init__(self):
        self._card1 = 'empty'
        self._card2 = 'empty'
    
    def _non_ace_card_value(self, card):
        return int(card.rank) if card.rank.isdigit() else self.COURT_CARD_VALUE

    @staticmethod
    def _ace_value(total):
        return 1 if total >= 11 else 11

    @property
    def total(self):
        cards = [self._card1, self._card2]
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

    def __str__(self):
        return str([self._card1, self._card2])

    def discard_cards(self):
        # STUB: Discards cards, resets instance variables.
        pass

    def add_card(self, card):
        if self._card1 == 'empty':
            self._card1 = card
        else:
            self._card2 = card

    def _calculate_aces(self):
        # STUB: Help calculate aces?
        pass

    # STUB:
    # Knows how to work with Card objects. Dependency?
    # has two cards, knows total
    # Can add a card
    # Can reset? (Discard cards?)
    # knows how to calculate aces?
    # Maybe don't need it?
    pass

class Participant:
    # STUB:
    # Can Hit or Stay
    # Bust
    # Has points
    # has hand (own class?)
    def __init__(self):
        self._hand = Hand()
        self._score = 0         # Overall score; game wins.

    @property
    def hand(self):
        return self._hand

    def hit_or_stay(self):
        pass

    def is_busted(self):
        # STUB:
        # Checks hand if busted?
        pass

    def points(self):
        self._hand.total

    pass

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self._deck = Deck()

    def shuffle_cards(self):
        self._deck.shuffle()

    def deal_cards(self, other):
        # STUB: Must deal card to self and player
        for _ in range(2):
            self._hand.add_card(self._deck.deal())
            other._hand.add_card(self._deck.deal())

    def hide_hand(self):
        pass

    def reveal_hand(self):
        pass

    # Can shuffle
    # Can deal
    # Can hide, reveal hand
    # Has:
        # A Deck of cards
        # points
    pass

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

    # Hit or stay etc
    # Has a hand
    # Has dollar amount
    pass

class TOGame:
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

    def _display_welcome_msg(self):
        print('Welcome to Twenty One!')

    def _display_goodbye_msg(self):
        print('Thank you for playing Twenty One! Goodbye.')

    def _show_cards(self):
        print(f'{self._dealer.hand} : {self._dealer.hand.total}')
        print(f'{self._player.hand} : {self._player.hand.total}')

    def play(self):
        self._display_welcome_msg()
        self._dealer.shuffle_cards()
        self._dealer.deal_cards(self._player)

        self._show_cards()
        # self._players_turn()
        # self._dealers_turn()
        # self._display_result()
        # self._play_again()
        self._display_goodbye_msg()
    pass

game = TOGame()
game.play()