import json

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

class CardDisplayMixin:
    def display(self, hidden=False):
        if not hidden:
            for l in CardAscii().card_ascii(self._suite, self._rank):
                print(l)
        else:
            for l in CardAscii().card_ascii():
                print(l)

class Card(CardDisplayMixin):
    def __init__(self, rank, suite):
        self._rank = rank
        self._suite = suite

    @property
    def rank(self):
        return self._rank

    @property
    def suite(self):
        return self._suite

hand = [Card('K', 'clubs'), Card('Q', 'hearts'), Card(10, 'hearts'), Card(5, 'spades')]
'''

I
- Card object
O
- a dictionary that can be printed out to print out cards horizontally

Rules:

E:

D:

notes:
- Cards can be printed out if we print each card line in the hand one by one rather 
than one card at a time.

A:
- Init a new list

> Loop through the indices of the card ascii display list:
    - Init an empty list
    >> Loop through each card object in the hand
        - append the element at current index of card list to empty list

    
c:
'''
def horizontal_display(hand):
    gap = '   '
    total_lines = len(CardAscii().card_ascii(hand[0].suite, hand[0].rank))

    for idx in range(total_lines):

        current_line = []
        for card in hand:
            current_line.append(CardAscii().card_ascii(card.suite, card.rank)[idx])

        print(gap.join(current_line))

horizontal_display(hand)