from BlackJack import ranks
from BlackJack import values


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values.get(card.rank)

        if card.rank == ranks[12]:
            self.aces += 1

    def adjust_ace(self):

        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        hand = ''
        for card in self.cards:
            hand += ',' + card.__str__()
        return hand
