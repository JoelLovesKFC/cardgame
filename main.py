import random

class Cards:
    def __init__(self):
        # Initialize suits with ranks as double arrays
        self.diamonds = [["Diamonds", rank] for rank in range(1, 14)]
        self.spades = [["Spades", rank] for rank in range(1, 14)]
        self.hearts = [["Hearts", rank] for rank in range(1, 14)]
        self.clubs = [["Clubs", rank] for rank in range(1, 14)]
        self.joker = [["Joker", rank] for rank in range(1,14)]
        self.deck = self.diamonds + self.spades + self.hearts + self.clubs + self.joker
    
    def random_card(self):
     return random.choice(self.deck)

cards = Cards() #creates object 
hand = [cards.random_card() for _ in range(5)]

print("Random Hand of 5 cards: ")
for card in hand: 
    print(card)
