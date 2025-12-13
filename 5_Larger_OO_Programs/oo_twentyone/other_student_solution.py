import random
import os
import time


def prompt(msg):
    print(f"==> {msg}")


def clear_screen():
    os.system("clear")


def display_underline():
    prompt("--------------------------------")


def press_to_continue():
    print()
    input("Press enter to continue: ")


class Hand:
    def __init__(self):
        self._cards = []

    @property
    def cards(self):
        return self._cards

    def add(self, card):
        self.cards.append(card)

    def reset(self):
        self._cards.clear()

    def value(self):
        ranks = [card.rank for card in self.cards if not card.hidden]
        if len(ranks) < 2:
            return "unknown"

        total = sum([card.value() for card in self.cards if not card.hidden])

        for _ in range(ranks.count("A")):
            if total > TwentyOneGame.TWENTY_ONE:
                total -= Card.FACE_VALUE

        return total

    def hide_card(self):
        self.cards[-1].hide()

    def reveal_card(self):
        self.cards[-1].reveal()

    def join_cards(self):
        return ", ".join([str(card) for card in self.cards])

    def is_busted(self):
        return self.value() > TwentyOneGame.TWENTY_ONE


class Card:
    FACE_CARDS = ("J", "Q", "K")
    FACE_VALUE = 10
    ACE_VALUE = 11

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
        self._hidden = False

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def hidden(self):
        return self._hidden

    def hide(self):
        self._hidden = True

    def reveal(self):
        self._hidden = False

    def __str__(self):
        if self._hidden:
            return "[hidden]"

        return f"{self.rank}{self.suit}"

    def value(self):
        if self.rank in self.__class__.FACE_CARDS:
            return self.__class__.FACE_VALUE

        if self.rank == "A":
            return self.__class__.ACE_VALUE

        return self.rank


class Deck:
    RANKS = tuple(range(2, 11)) + ("J", "Q", "K", "A")
    SUITS = ("♥", "♦", "♣", "♠")

    def __init__(self):
        self.reset()

    def reset(self):
        cards = [
            Card(rank, suit)
            for rank in self.__class__.RANKS
            for suit in self.__class__.SUITS
        ]
        random.shuffle(cards)
        self.cards = cards

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards):
        self._cards = cards

    def deal_card(self, participant):
        participant.hand.add(self.cards.pop())


class Player:
    def __init__(self, balance):
        self._hand = Hand()
        self.balance = balance

    @property
    def hand(self):
        return self._hand

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def increase_balance(self):
        self.balance += 1

    def decrease_balance(self):
        self.balance -= 1

    def reset_balance(self, balance):
        self.balance = balance

    def is_broke(self):
        return self.balance == 0

    def is_rich(self):
        return self.balance == 10


class Dealer:
    def __init__(self):
        self._hand = Hand()

    @property
    def hand(self):
        return self._hand


class TwentyOneGame:
    PLAYER_BALANCE = 5
    WINNING_BALANCE = PLAYER_BALANCE * 2
    DECK_PENETRATION = 0.75 # playing with 75% penetration before reshuffle
    CARDS_LEFT = int(52 * (1 - DECK_PENETRATION))
    DEALER_STAY = 17
    TWENTY_ONE = 21

    def __init__(self):
        self.deck = Deck()
        self.player = Player(TwentyOneGame.PLAYER_BALANCE)
        self.dealer = Dealer()

    @classmethod
    def display_welcome_message(cls):
        clear_screen()
        prompt("Welcome to Twenty One!")
        prompt(
            f"Your player balance is ${cls.PLAYER_BALANCE}. "
            "Each round requires a bet of $1."
        )
        prompt(
            "The game will end when you go broke "
            f"or double your balance to ${cls.WINNING_BALANCE}."
        )
        prompt("Good luck!")
        press_to_continue()

    @staticmethod
    def display_goodbye_message():
        clear_screen()
        prompt("Thank you for playing. See you next time!")

    @staticmethod
    def _validate_decision(decision):
        while decision not in ("h", "hit", "s", "stay"):
            prompt("Not a valid decision. Would you like to (h)it or (s)tay?")
            decision = input().strip().lower()

        return decision

    @staticmethod
    def _validate_answer(answer):
        while answer not in ("y", "yes", "n", "no"):
            prompt("Not a valid answer. Would you like to play again (y/n)?")
            answer = input().strip().lower()

        return answer

    def deal_cards(self):
        for _ in range(2):
            self.deck.deal_card(self.player)
            self.deck.deal_card(self.dealer)

        self.dealer.hand.hide_card()

    def display_hands(self):
        prompt(f"Dealer's hand: {self.dealer.hand.join_cards()}")
        prompt(f"Player's hand: {self.player.hand.join_cards()}")
        display_underline()

    def display_hand_values(self):
        prompt(f"Dealer's total is {self.dealer.hand.value()}")
        prompt(f"Player's total is {self.player.hand.value()}")
        display_underline()

    def main_screen(self):
        clear_screen()
        self.display_balance()
        display_underline()
        self.display_hands()
        self.display_hand_values()

    def reshuffle_if_low(self):
        cards_remaining = len(self.deck.cards)
        # allows dealing up to 39 cards (75% penetration) before reshuffle
        if cards_remaining <= TwentyOneGame.CARDS_LEFT:
            clear_screen()
            prompt(f"There are only {cards_remaining} cards left in the deck.")
            prompt("Shuffling new deck for the next round...")
            press_to_continue()
            self.deck.reset()

    def new_round(self):
        self.dealer.hand.reset()
        self.player.hand.reset()
        self.reshuffle_if_low()

    def player_turn(self):
        while True:
            self.main_screen()
            prompt("Would you like to (h)it or (s)tay? ")
            decision = input().strip().lower()
            decision = TwentyOneGame._validate_decision(decision)

            if decision in ("hit", "h"):
                prompt("Player hits. Dealing card...")
                time.sleep(1)
                self.deck.deal_card(self.player)

            if self.player.hand.is_busted() or (decision in ("s", "stay")):
                break

        self.main_screen()
        if decision in ("s", "stay"):
            prompt("Player decides to stay.")
            press_to_continue()

    def dealer_turn(self):
        self.dealer.hand.reveal_card()

        while True:
            if self.player.hand.is_busted():
                break

            self.main_screen()

            if self.dealer.hand.value() >= TwentyOneGame.DEALER_STAY:
                break

            if self.dealer.hand.value() < TwentyOneGame.DEALER_STAY:
                prompt("Dealer hits. Dealing card...")
                time.sleep(1)
                self.deck.deal_card(self.dealer)

    def determine_result(self):
        result = ""

        if self.player.hand.is_busted():
            result = "player_bust"
        elif self.dealer.hand.is_busted():
            result = "dealer_bust"
        elif self.player.hand.value() > self.dealer.hand.value():
            result = "player_win"
        elif self.dealer.hand.value() > self.player.hand.value():
            result = "dealer_win"
        else:
            result = "tie"

        return result

    def update_balance(self):
        match self.determine_result():
            case "player_bust":
                self.player.decrease_balance()
            case "dealer_bust":
                self.player.increase_balance()
            case "player_win":
                self.player.increase_balance()
            case "dealer_win":
                self.player.decrease_balance()

    def display_result(self):
        match self.determine_result():
            case "player_bust":
                prompt("Player busts. Dealer wins!")
            case "dealer_bust":
                prompt("Dealer busts. Player wins!")
            case "player_win":
                prompt("Player wins!")
            case "dealer_win":
                prompt("Dealer wins!")
            case "tie":
                prompt("It's a tie!")

        press_to_continue()

    def display_balance(self):
        prompt(f"Player's current balance: ${self.player.balance}")

    def play_again(self):
        prompt("Would you like to play again (y/n)?")
        answer = input().strip().lower()
        answer = TwentyOneGame._validate_answer(answer)

        return answer in ("yes", "y")

    def start(self):
        TwentyOneGame.display_welcome_message()

        while True:
            self.player.reset_balance(TwentyOneGame.PLAYER_BALANCE)

            while not (self.player.is_broke() or self.player.is_rich()):
                self.new_round()
                self.deal_cards()
                self.player_turn()
                self.dealer_turn()
                self.update_balance()
                self.main_screen()
                self.display_result()

            if not self.play_again():
                break

        TwentyOneGame.display_goodbye_message()


game = TwentyOneGame()
game.start()