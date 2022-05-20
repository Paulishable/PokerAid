"""Poker aid main driver"""

import math
from hand_rating import *
from probability_calcs import *
from card_utilities import *


# 2598960 all possible
# 1296424 all hands with at least 2 pair
def all_good_hands_lister(all_hands):
    """find all possible hands with at least 2 pair"""

    with open("possible_hand_list.txt", "w") as data_file:
        for i in range(1296424):

            if i % 1000 == 0:
                print(str(i))

            this_hand = []
            # one_hand = []
            one_hand = deal(this_hand)
            # print(one_hand)
            # all_possible_hands.append(one_hand)
            # all_possible_hands[-1] = deal(one_hand)

            if keep_the_hand(one_hand):
                if one_hand not in all_hands:
                    all_hands.append(one_hand)
                    data_file.write(f"{all_hands[-1]}\n")
                # print_and_rate_it(one_hand)
                else:
                    one_hand = deal(this_hand)
                    if keep_the_hand(one_hand):
                        all_hands.append(deal(one_hand))
                        data_file.write(f"{all_hands[-1]}\n")
                    # print_and_rate_it(one_hand)

        # print(deal(one_hand))
    return all_hands


def print_and_rate_it(current_hand):
    print("\n")
    for item in range(5):
        print(find_card_face_string(current_hand[item]) + " of " + find_card_suit(current_hand[item]))
    print("")
    print(rate_the_hand(current_hand))

my_hand = deal(a_hand)
print(my_hand)
print_and_rate_it(my_hand)


# all_hands_lister(all_possible_hands)

a_hand_from_file = []
with open("possible_hand_list.txt", "r") as data_file:
    a_hand_from_file.append(data_file.readline().rstrip())
    print(a_hand_from_file[0])

print(number_of_good_hands())
