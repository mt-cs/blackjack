from random import shuffle 

# Global constant for the winning number of cards
MAX = 21

# main function
def main():
    # Local variables
    hand1 = 0
    hand2 = 0
    deck = create_deck()

    # Create a list from deck
    deckList = list(deck.items())

    # Deal a card to each player and calculate hand value.
    while hand1 <= MAX and hand2 <= MAX:
        shuffle(deckList)
        card, value = deckList.pop()
        hand1=update_hand_value(hand1,value,card) 
        print ('Player 1 was dealt:',card)

        card, value = deckList.pop()
        shuffle(deckList)
        hand2=update_hand_value(hand2,value,card) 
        print ('Player 2 was dealt:',card)

    # Display hand value
    print('Player 1 hand has:',hand1)
    print('Player 2 hand has:',hand2)

    # Determine the winner.
    if hand1 > MAX and hand2 > MAX:
        print ('There is no winner')
    elif hand1 > MAX:
        print ('Player 1 wins')
    elif hand2 > MAX:
        print('Player 2 wins')
main()

# The create_deck function creates a deck of cards and
# returns the deck.
def create_deck():
    # Set up local variables
    suits = ['Spades','Hearts','Clubs','Diamonds']
    special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

    # Create list of all the card values
    numbers = ['Ace', 'King', 'Queen', 'Jack']
    for i in range(2,11):
        numbers.append(str(i))
    
    # Initialize deck
    deck = {}
    for suit in suits:
        for num in numbers:
            # Add the numbers 2-10 to the deck
            if num.isdigit() == True:
                deck[suit+" of "+str(num)]=int(num)
            # Add the Ace, King, Queen, or Jack values to the deck
            elif num in special_values.keys():
                deck[suit+" of "+num]=special_values.get(num)
    return deck

# If a player is dealt an ace, the program should decide the value by:
# The ace will be worth 11 points, unless that makes the player's hand exceed 21 points.
# In that case the ace will be worth 1 point.
def update_hand_value(hand, value, card):
    if 'Ace' in card:
        if hand+value<=MAX:
            value = 11
    hand += value
    return hand


