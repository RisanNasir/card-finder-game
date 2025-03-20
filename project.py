import random, sys
from PIL import Image, ImageTk
import gui 

# Basic card class for a card
class Card:
    def __init__(self, rank, suit): # constructor for the card object.
        self.suit = suit
        self.rank = rank
    def __str__(self):  # string representation of the current card object.
        return f"{self.rank}_of_{self.suit}"
    def get_card(self):
        return f"{self.rank}_of_{self.suit}"
    
    @property   # Getters and setter for the card values.
    def suit(self):
        return self._suit
    @suit.setter
    def suit(self, suit):
        if not suit in ["spades", "hearts", "diamonds", "clubs"]:
            raise ValueError("Invalid Value")
        self._suit = suit
    @property
    def rank(self):
        return self._rank
    @rank.setter
    def rank(self, rank):
        if not rank in range(2,15):
            raise ValueError("Invalid Value")
        self._rank = rank

# Function to make an initial standard deck without shuffle.
def populate_std_deck():
    deck = []
    suits = ["spades", "hearts", "clubs", "diamonds"]
    for suit in suits:
        for i in range(2, 15):
            deck.append(Card(i, suit))
    return deck

# Shuffle the given deck of cards.
def shuffle_deck(deck):
    shuffled = []
    while deck:
        card = random.choice(deck)
        shuffled.append(card)
        deck.remove(card)
    return shuffled

# This method splits shuffled deck in to three lists of cards and return them.
def three_musketeers(deck):
    left, right, center = [], [], []
    for i in range(0,49, 3):
        left.append(deck[i])
        center.append(deck[i+1])
        right.append(deck[i+2])
    left.append(deck[51])
    return [left, center, right] # returning list of lists.

# This method is to rearrange the three lists into a complete deck in specific order.
def rearrange_deck(left, center, right):
    deck = []
    for card in left:
        deck.append(card)
    for card in center:
        deck.append(card)
    for card in right:
        deck.append(card)
    return deck
# This function arranged a deck in an order where picked line will be put in middle.
def play_game(deck, choice):
    left, right, center = [], [], []
    try:
        musketeer1, musketeer2, musketeer3 = three_musketeers(deck)
        if choice == 1: # if chosen card in 1st line
            left = musketeer2
            center = musketeer1
            right = musketeer3
        elif choice == 2: # if chosen card in 2nd line
            left = musketeer1
            center = musketeer2
            right = musketeer3
        elif choice == 3: # if chosen card is in 3rd line
            left = musketeer1
            center = musketeer3
            right = musketeer2
        deck = rearrange_deck(left, center, right) # rearrange the deck in desired format
        return deck, center[8] # returning the arranged deck and the card which should be the chosen one.
    except ValueError:
        print("Invalid value")
        sys.exit(1)

# function to resize the image
def resize_image(name, x=0, y=0):
    global final_image
    name = f'cardimages/{name}.png'
    cardimage = Image.open(name)
    if x==0 and y==0:
        final_image = ImageTk.PhotoImage(cardimage)
        return final_image
    else:
        resized_image = cardimage.resize((x, y))
        final_image = ImageTk.PhotoImage(resized_image)
        return final_image

def main():
    deck = populate_std_deck()
    gui.card_game_gui(deck)

if __name__ == "__main__":
    main()
