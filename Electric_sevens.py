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
deck = list(itertools.product(range(1,14),['SPADE','HEART','DIAMOND','CLUB']))

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
    print('Current Spades: ' + str(played_spade))
    print('Current Hearts: ' + str(played_heart))
    print('Current Diamonds: ' + str(played_heart))
    print('Current Clubs: ' + str(played_club))
