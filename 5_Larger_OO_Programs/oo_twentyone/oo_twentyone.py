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

    def deal_one(self):
        if self._deck:
            return self._deck.pop()
        return None
    
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
    
    def _non_ace_card_value(self, card):
        return int(card.rank) if card.rank.isdigit() else self.COURT_CARD_VALUE

    @staticmethod
    def _ace_value(total):
        '''
        Returns 11 or 1 which are the possible values of an Ace.
        '''
        return 1 if total >= 11 else 11

    @property
    def hidden_total(self):
        card2 = self._cards[1]
        if card2.rank != 'A':
            return self._non_ace_card_value(card2)
        else: 
            return self.ACE_VALUE

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

    def __str__(self):
        return str([self._cards])
    
    @property
    def hidden_hand(self):
        return str([self._cards[0].hide()] + [self._cards[1]])

    def discard_cards(self):
        # STUB: Discards cards, resets instance variables.
        pass

    def add_card(self, card):
        self._cards.append(card)

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

    def is_busted(self):
        return self._hand.total > 21

    def points(self):
        self._hand.total

    pass

class Dealer(Participant):
    STAY_LIMIT = 17

    def __init__(self):
        super().__init__()

    def hit_or_stay(self):
        if self._hand.total >= Dealer.STAY_LIMIT:
            return 'stays'
        else:
            return 'hits'

    # Can shuffle
    # Can deal
    # Can hide, reveal hand
    # Has:
        # A Deck of cards
        # points

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

    # Hit or stay etc
    # Has a hand
    # Has dollar amount
    pass

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
            player1.hand.add_card(self._deck.deal_one())
            player2.hand.add_card(self._deck.deal_one())
    
    # def _deal_one_card(self):
    #     card = self._deck.deal_one()
    #     if card:
    #         return card
    #     else:
    #         print('Deck is empty!')

    def _show_cards(self, reveal=False):
        dealers = self._dealer.hand
        players = self._player.hand

        if reveal:
            print(f'{dealers} : {dealers.total}')
        else:
            print(f'{dealers.hidden_hand} : {dealers.hidden_total}')
        print(f'{players} : {players.total}')

    def _players_turn(self):
        # STUB:
        # Player can choose hit or stay
        # Player can bust if goes over the total
        # Give player option to choose or stay, does hand need to be list??
        # loop?
        player = self._player
        while True:
            choice = player.hit_or_stay()
            print(f'Player {choice}!')
            if choice == 'hits':
                player.hand.add_card(self._deck.deal_one())
            else:
                break

            if player.is_busted():
                print('Player Busts!')
                break
            self._show_cards()

    def _dealers_turn(self):
        dealer = self._dealer
        print('Dealers Hand revealed:')
        self._show_cards(reveal=True)

        while True:
            choice = dealer.hit_or_stay()
            print(f'Dealer {choice}!')
            if choice == 'hits':
                dealer.hand.add_card(self._deck.deal_one())
            else:
                break

            if dealer.is_busted():
                print('Dealer busts!')
                break
            self._show_cards(reveal=True)

    def play(self):
        self._display_welcome_msg()
        self._shuffle_cards()
        self._deal_cards(self._player, self._dealer)

        self._show_cards()

        self._players_turn()
        
        self._dealers_turn()
        # self._display_result()
        # self._play_again()
        self._display_goodbye_msg()
    pass

game = TOGame()
game.play()

# Busted outcome doesnt end game yet