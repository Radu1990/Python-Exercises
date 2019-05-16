import random


class Card:
    """Represents a standard playing card.
        Attributes:
          suit: integer 0-3
          rank: integer 1-13
        """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    """
    # one implementation of __lt__ 
    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False
        # if suits are the same then check ranks
        return self.rank < other.rank
    """
    # second implementation with tuples
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    """Represents a Deck of cards master class"""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    # (1) method to remove a card from the deck
    # (from the bottom of the list) and return it
    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.
        i: index of the card to pop; by default, pops the last card."""
        return self.cards.pop(i)

    # (2) method to add card
    def add_card(self, card):
        self.cards.append(card)

    # (3) method to shuffle the cards
    def shuffle(self):
        random.shuffle(self.cards)

    # (4) method to sort the cards in a Deck
    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    # (5) method to move cards from deck to a hand
    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.
        hand: destination Hand object
        num: integer number of cards to move"""
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, nr_hands, nr_cards):
        hands_lst = []
        for x in range(nr_hands):
            hands_lst.append()


class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label


hand_1 = Deck()
hand_1.deal_hands(4, 5)