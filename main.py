"""Poker aid main driver"""

import math
from hand_rating import *
from probability_calcs import *
from card_utilities import *

# 2598960
def all_hands_lister(all_hands):
    """find all possible hands"""
    for i in range(2598960):

        if i % 1000 == 0:
            print(str(i))

        this_hand = []
        # one_hand = []
        one_hand = deal(this_hand)
        # print(one_hand)
        # all_possible_hands.append(one_hand)
        # all_possible_hands[-1] = deal(one_hand)

        if one_hand not in all_hands:
            # print("not in")
            all_hands.append(one_hand)
        else:
            one_hand = deal(this_hand)
            all_hands.append(deal(one_hand))
    # print(deal(one_hand))
    return all_hands


my_hand = deal(a_hand)
print(my_hand)

# my_hand[0] = 10
# my_hand[1] = 10
# my_hand[2] = 9
# my_hand[3] = 13
# my_hand[4] = 52
print("\n")
for item in range(5):
    print(find_card_face_string(my_hand[item]) + " of " + find_card_suit(my_hand[item]))
print("")
print(rate_the_hand(my_hand))

