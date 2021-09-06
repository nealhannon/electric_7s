# welcome the players, advise to look at readme for rules, and establish number of players
print('Welcome to Electric 7\'s! Look at the README for how to play information and rules.')

num_players = input('Please enter the number of players between 3 and 8: ')
while int(num_players) < 3 or int(num_players) > 8:
    print('Sorry this game only supports 3 - 8 players.')
    num_players = input('Please enter the number of players between 3 and 8: ')
print('We have ' + str(num_players) + ' players! Lets get started')