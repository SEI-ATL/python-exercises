class Deck:
    def __init__(self):
        self.deck_val = '23456789TJQKA'
        self.deck_suit = 'CDHS'
        self.full_deck = [
            ''.join([val, suit])
            for suit in self.deck_suit
            for val in self.deck_val
        ]
        self.shuffle_deck()
    def shuffle_deck(self):
        random.shuffle(self.full_deck)
        return self.full_deck
    def draw(self, n):
        cards = []
        for i in range(n):
            cards.append(self.full_deck.pop(0))
        return cards