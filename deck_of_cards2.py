import random
#Creates list of card and prints the length of the list
deck_of_cards = ['Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts']
print(f"Cards currently in the deck: {len(deck_of_cards)}\n")
weston = 51
count = 0

for number_of_hands in range(1, 4):
    print(f"The next 3 cards are part of hand {number_of_hands}")
    hand = []
    for value in range(1, 4):
        random_number = random.randint(0, weston)
        card = deck_of_cards[random_number]
        hand.append(card)
        if card == 'Ace of Spades' or card == 'Ten of Spades' or card == 'Jack of Spades' or card == 'Queen of Spades' or card == 'King of Spades' or card == 'Ace of Diamonds' or card =='Ten of Diamonds' or card == 'Jack of Diamonds' or card =='Queen of Diamonds' or card == 'King of Diamonds' or card == 'Ace of Clubs' or card == 'Ten of Clubs' or card == 'Jack of Clubs' or card == 'Queen of Clubs' or card == 'King of Clubs' or card =='Ace of Hearts' or card == 'Ten of Hearts' or card == 'Jack of Hearts' or card == 'Queen of Hearts' or card =='King of Hearts':
            count = count + 1
        elif card == '2 of Spades' or card == '3 of Spades' or card == '4 of Spades' or card == '5 of Spades' or card == '6 of Spades' or card == '2 of Diamonds' or card == '3 of Diamonds' or card == '4 of Diamonds' or card == '5 of Diamonds' or card == '6 of Diamonds' or card == '2 of Clubs' or card == '3 of Clubs' or card == '4 of Clubs' or card == '5 of Clubs' or card == '6 of Clubs' or card == '2 of Hearts' or card == '3 of Hearts' or card == '4 of Hearts' or card == '5 of Hearts' or card == '6 of Hearts':
            count = count - 1
        deck_of_cards.pop(random_number)
        weston = weston - 1
    print(hand)
    print('\n')
print(f"These cards remain in the deck: {deck_of_cards}")
print(f"The current count is: {count}")
