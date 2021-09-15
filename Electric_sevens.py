# import modules being used
import itertools, random, math

# # welcome the players, advise to look at readme for rules, and establish number of players
print('Welcome to Electric 7\'s! Look at the README for how to play information and rules.')

num_players = input('Please enter the number of players between 3 and 6: ')
while int(num_players) < 3 or int(num_players) > 6:
    print('Sorry this game only supports 3 - 6 players.')
    num_players = input('Please enter the number of players between 3 and 6: ')
print('We have ' + str(num_players) + ' players! Lets get started')

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

def deal_cards(deck, num_players):
    n = math.ceil(len(deck)/num_players)
    for x in range(0, len(deck), n):
        hand = deck[x: n+x]
        if len(hand) < n:
            hand = hand + [None for y in range(n-len(deck))]
        yield hand
    
player_hands = deal_cards(deck, int(num_players))
player_hands_list = list(player_hands)

player1_hand = (player_hands_list[0])
player2_hand = (player_hands_list[1])
player3_hand = (player_hands_list[2])
if int(num_players) >= 4:
    player4_hand = (player_hands_list[3])
if int(num_players) >= 5:
    player5_hand = (player_hands_list[4])
if int(num_players) == 6:
    player6_hand = (player_hands_list[5])

#function to show cards on playing field
def show_field():
    played_spade.sort()
    played_heart.sort()
    played_diamond.sort()
    played_club.sort()
    return ('Current Spades: ' + str(played_spade)), ('Current Hearts: ' + str(played_heart)),\
    ('Current Diamonds: ' + str(played_diamond)), ('Current Clubs: ' + str(played_club))

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

#functions for player turns
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
    print(show_field())
    print('Your hand: ' + str(player_hand))
    player_card = input('What card would you like to play? (# of Suit) ')
    while player_card.upper() not in str(player_hand):
        print('Sorry you dont have that card in your hand.')
        player_card = input('What card would you like to play? (# of Suit)')
    player_card_index = player1_hand.index(player_card.upper())
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

