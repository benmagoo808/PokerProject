from Classes import Deck
from Classes import Card
import re

total_cards = []
hand_count = 0

def start_new_hand():
    new_hand = Deck()
    new_hand.shuffle()
    hand = new_hand.deal_hand()
    new_hand.burn_card()
    flop = new_hand.deal_flop()
    new_hand.burn_card()
    turn = new_hand.deal_turn()
    new_hand.burn_card()
    river = new_hand.deal_river()
    community = new_hand.community_cards
    print('Your hand is:\n' + str(hand))
    print('The flop is:\n' + str(flop))
    print('The Turn comes:\n' + str(turn))
    print('The River shows:\n' + str(river) + '\n\nFor a table '
                    'of:\n\n' + str(community))

    return total_cards.append(hand + community)


def detect_flush():
    flush = ''.join(total_cards[hand_count])

    if len(re.findall('Hearts', flush)) > 4:
        return True
    elif len(re.findall('Diamonds', flush)) > 4:
        return True
    elif len(re.findall('Spades', flush)) > 4:
        return True
    elif len(re.findall('Clubs', flush)) > 4:
        return True
    else:
        return False


start_new_hand()
if detect_flush() == True:
    print('Flush!!')
else:
    print('No Flush!!')