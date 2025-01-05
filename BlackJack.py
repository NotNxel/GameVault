# GameVault - A Treasure Trove of Minigames  
# Featuring classics like Russian Roulette, Blackjack, and JoJo-inspired adventures!  
# Created with passion by Neel  
# Explore more: https://github.com/YourUsername/GameVault  
# © 2025 Neel. All rights reserved.  


import random
from termcolor import colored

# Define card values and suits
suits = ['♠', '♥', '♦', '♣']
suit_colors = {'♠': 'black', '♣': 'black', '♥': 'red', '♦': 'red'}
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
value_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Function to create a deck of cards
def create_deck():
    deck = [(value, suit) for suit in suits for value in values]
    random.shuffle(deck)
    return deck

# Function to calculate the total score of a hand
def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        score += value_map[card[0]]
        if card[0] == 'A':
            aces += 1
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

# Function to print cards in ASCII art
def print_card(value, suit):
    card = f"""
+--------+
| {value: <2} {suit: <2} |
|        |
|   {suit}   |
+--------+
"""
    print(colored(card, suit_colors[suit]))

# Function to print hands in ASCII art
def print_hand(player, hand):
    print(f"{player} hand:")
    for card in hand:
        print_card(card[0], card[1])

# Function for the main game logic
def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Show initial hands
    print_hand("Player", player_hand)
    print(colored(f"Dealer's hand: {dealer_hand[0][0]}{colored(dealer_hand[0][1], suit_colors[dealer_hand[0][1]])} and a hidden card", 'blue'))

    # Player's turn
    while calculate_score(player_hand) < 21:
        choice = input(colored("Do you want to hit or stand? (h/s): ", 'green')).lower()
        if choice == 'h':
            player_hand.append(deck.pop())
            print_hand("Player", player_hand)
        elif choice == 's':
            break
        else:
            print(colored("Invalid choice! Please choose 'h' for hit or 's' for stand.", 'red'))

    player_score = calculate_score(player_hand)
    if player_score > 21:
        print(colored("Player busts! You lose.", 'red'))
        return

    # Dealer's turn
    print_hand("Dealer", dealer_hand)
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print_hand("Dealer", dealer_hand)
    dealer_score = calculate_score(dealer_hand)

    # Determine winner
    print(colored(f"Player score: {player_score}, Dealer score: {dealer_score}", 'yellow'))
    if dealer_score > 21:
        print(colored("Dealer busts! You win.", 'green'))
    elif player_score > dealer_score:
        print(colored("You win!", 'green'))
    elif player_score < dealer_score:
        print(colored("You lose!", 'red'))
    else:
        print(colored("It's a tie!", 'blue'))

# Start the game
if __name__ == '__main__':
    play_blackjack()
