import unittest

import random

dealer_cards = []

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 10))
    if len(dealer_cards) == 2:
        print('Dealer has X &', dealer_cards[1])

player_cards = []

while len(player_cards) != 2:
    player_cards.append(random.randint(1, 10))
    if len(player_cards) == 2:
        print('You have' , player_cards)

#dealer hand
if sum(dealer_cards) == 21:
    print('Dealer has BlackJack House wins again!')
elif sum(dealer_cards) > 21:
    print('Dealer has busted!')

# Player hand(your hand)
while sum(player_cards) < 21:
    action_taken = str(input('do you want to stay or hit? '))
    if action_taken == 'hit':
        player_cards.append(random.randint(1, 10))
        print('You now have a total of  '+ str(sum(player_cards)) +' from these cards', player_cards)
    else:
        print('You win!')

        break

if sum(player_cards) > 21:
    print('You Busted! Dealer wins.')

elif sum(player_cards) <= 21:

    print('You have 21! You Win!!')

#next i need to create a split cards call
#I need to create a loop to come back and give a card to the dealer after players gets last cards.
#i need to create where if a player is less than 21 than the dealer needs to get another card if the dealer has less
# 17 but stays if they have over 18 only the players with more but not over 21 wins but if the same as dealer than push