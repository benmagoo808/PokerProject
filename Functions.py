from Classes import Deck
total_cards = []

def start_new_hand():
    while True:
        print('Press "Return" to deal, "E" to exit:  ')
        if input() == 'e':
            break
        else:
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
            input()
            print('The flop is:\n' + str(flop))
            input()
            print('The Turn comes:\n' + str(turn))
            input()
            print('The River shows:\n' + str(river) + '\n\nFor a table '
                    'of:\n\n' + str(community))
            total_cards.append(hand + community)

            return total_cards

def compare_hand():
    print(str(hand))

start_new_hand()
print(total_cards)