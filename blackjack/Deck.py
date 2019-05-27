from random import shuffle

from BlackJack import ranks
from BlackJack import suits
from Card import Card


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):
        shuffle(self.deck)

    def __str__(self):
        return ",".join(map(str, self.deck))
