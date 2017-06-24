from Classes import Deck
import re
from collections import Counter



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


def detect_multiple():
    ranks = []
    for i in range(len(total_cards[hand_count])):
        card = total_cards[hand_count][i].split('-')
        ranks.append(card[0])

    c = Counter(ranks)
    multiples = c.most_common(2)

    if multiples[0][1] == 2:
        return str('Pair of ' + multiples[0][0] + "'s ")
    elif multiples[0][1] == 2 and multiples[1][1] == 2:
        return str('Two Pair of ' + multiples[0][0] + "'s and " +
                     multiples[1][0] + "'s ")
    elif multiples[0][1] == 3:
        return str('Three of a kind ' + multiples[0][0] + "'s ")
    elif multiples[0][1] == 4:
        return str('Four of a kind ' + multiples[0][0] + "'s ")
    elif multiples[0][1] == 3 and multiples[1][1] == 2:
        return str('Full House, ' + multiples[0][0] + "'s over " +
                   multiples[1][0] + "'s ")

    else:
        return False



start_new_hand()
print(detect_multiple())

