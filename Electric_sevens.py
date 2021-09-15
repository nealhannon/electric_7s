# import modules being used
import random, re

# # welcome the players, advise to look at readme for rules, and establish number of players
print('Welcome to Electric 7\'s! Look at the README for how to play information and rules.')
print()
num_players = input('Please enter the number of players between 3 and 6: ')
while int(num_players) < 3 or int(num_players) > 6:
    print('Sorry this game only supports 3 - 6 players.')
    num_players = input('Please enter the number of players between 3 and 6: ')
print('We have ' + str(num_players) + ' players! Lets get started')
print()

#Deal cards to players and establish playing field
card_numbers = range(1,14)
card_suits = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']
def create_deck():
    deck = []
    for number in card_numbers:
        for suit in card_suits:
            deck.append(str(number) + ' OF ' + suit)
    return deck

deck = create_deck()

spade_str = 'SPADES'
heart_str = 'HEARTS'
diamond_str = 'DIAMOND'
club_str = 'CLUB'

played_spade = []
played_heart = []
played_diamond = []
played_club = []

played_spade.append(deck.pop(24))
played_heart.append(deck.pop(24))
played_diamond.append(deck.pop(24))
played_club.append(deck.pop(24))

random.shuffle(deck)

player1_hand = []
player2_hand = []
player3_hand = []
player4_hand = []
player5_hand = []
player6_hand = []

def deal_cards(deck, num_players):
    while len(deck) > 0:
        player1_hand.append(deck.pop(0))
        player2_hand.append(deck.pop(0))
        player3_hand.append(deck.pop(0))
        if num_players >= 4 and len(deck) > 0:
            player4_hand.append(deck.pop(0))
        if num_players >= 5 and len(deck) > 0:
            player5_hand.append(deck.pop(0))
        if num_players == 6 and len(deck) > 0:
            player6_hand.append(deck.pop(0))
    return player1_hand, player2_hand, player3_hand, player4_hand, player5_hand, player6_hand

    
#function to sort and show cards on playing field
import re
def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)',text) ]

def show_field():
    played_spade.sort(key=natural_keys)
    played_heart.sort(key=natural_keys)
    played_diamond.sort(key=natural_keys)
    played_club.sort(key=natural_keys)
    print('Current Spades: ' + str(played_spade))
    print('Current Hearts: ' + str(played_heart))
    print('Current Diamonds: ' + str(played_diamond))
    print('Current Clubs: ' + str(played_club))
    print()

#function to determine drinks
def drink_counter(suit):
    if suit == spade_str:
        drinks = len(played_spade)
        spade_num_list = []
        for cards in played_spade:
            cards_stripped = cards.strip(' OF SPADES')
            spade_num_list.append(int(cards_stripped))
        spade_num_list.sort()
        spade_range = list(range(spade_num_list[0], spade_num_list[-1] + 1))
        if spade_num_list == spade_range:
            return 'Give out ' + str(drinks) + ' drinks!'
        else:
            return 'Take ' + str(spade_num_list[-1] - spade_num_list[0] + 1) + ' drinks!'
    elif suit == heart_str:
        drinks = len(played_heart)
        heart_num_list = []
        for cards in played_heart:
            cards_stripped = cards.strip(' OF HEARTS')
            heart_num_list.append(int(cards_stripped))
        heart_num_list.sort()
        heart_range = list(range(heart_num_list[0], heart_num_list[-1] + 1))
        if heart_num_list == heart_range:
            return 'Give out ' + str(drinks) + ' drinks!'
        else:
            return 'Take ' + str(heart_num_list[-1] - heart_num_list[0] + 1) + ' drinks!'
    elif suit == diamond_str:
        drinks = len(played_diamond)
        diamond_num_list = []
        for cards in played_diamond:
            cards_stripped = cards.strip(' OF DIAMONDS')
            diamond_num_list.append(int(cards_stripped))
        diamond_num_list.sort()
        diamond_range = list(range(diamond_num_list[0], diamond_num_list[-1] + 1))
        if diamond_num_list == diamond_range:
            return 'Give out ' + str(drinks) + ' drinks!'
        else:
            return 'Take ' + str(diamond_num_list[-1] - diamond_num_list[0] + 1) + ' drinks!'
    else:
        drinks = len(played_club)
        club_num_list = []
        for cards in played_club:
            cards_stripped = cards.strip(' OF CLUBS')
            club_num_list.append(int(cards_stripped))
        club_num_list.sort()
        club_range = list(range(club_num_list[0], club_num_list[-1] + 1))
        if club_num_list == club_range:
            return 'Give out ' + str(drinks) + ' drinks!'
        else:
            return 'Take ' + str(club_num_list[-1] - club_num_list[0] + 1) + ' drinks!'

#function for player turns
def player_turn(player):
    if player == 1:
        player_hand = player1_hand
    elif player == 2:
        player_hand = player2_hand
    elif player == 3:
        player_hand = player3_hand
    elif player == 4:
        player_hand = player4_hand
    elif player == 5:
        player_hand = player5_hand
    else:
        player_hand = player6_hand
    show_field()
    print('Your hand: ' + str(player_hand))
    print()
    player_card = input('What card would you like to play? (# of Suit) ')
    while player_card.upper() not in str(player_hand):
        print('Sorry you dont have that card in your hand.')
        player_card = input('What card would you like to play? (# of Suit)')
    player_card_index = player_hand.index(player_card.upper())
    if spade_str in player_card.upper():
        played_spade.append(player_hand.pop(player_card_index))
        print(drink_counter(spade_str))
    elif heart_str in player_card.upper():
        played_heart.append(player_hand.pop(player_card_index))
        print(drink_counter(heart_str))
    elif diamond_str in player_card.upper():
        played_diamond.append(player_hand.pop(player_card_index))
        print(drink_counter(diamond_str))
    else:
        played_club.append(player_hand.pop(player_card_index))
        print(drink_counter(club_str))
    print()

#function to play
def play_game():
    deal_cards(deck, int(num_players))
    game_counter = 0
    while game_counter < 48:
        print('Player 1\'s turn:')
        player_turn(1)
        game_counter += 1
        if game_counter == 48:
            break
        print('Player 2\'s turn:')
        player_turn(2)
        game_counter += 1
        if game_counter == 48:
            break
        print('Player 3\'s turn:')
        player_turn(3)
        game_counter += 1
        if game_counter == 48:
            break
        if int(num_players) >= 4:
            print('Player 4\'s turn:')
            player_turn(4)
            game_counter += 1
            if game_counter == 48:
                break
        if int(num_players) >= 5:
            print('Player 5\'s turn:')
            player_turn(5)
            game_counter += 1
            if game_counter == 48:
                break
        if int(num_players) == 6:
            print('Player 6\'s turn:')
            player_turn(6)
            game_counter += 1    
    print()        
    print('GAME OVER! THANK YOU FOR PLAYING! FEEL FREE TO RESTART THE PROGRAM TO PLAY AGAIN!')
    print()

play_game()
