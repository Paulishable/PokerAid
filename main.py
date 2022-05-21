"""Poker aid main driver"""
import math
from probability_calcs import *
from card_utilities import *
from hand_rating import *
import re

the_cards = []
all_possible_hands = []
a_hand = []
hash_list = []


def deal(the_hand):
    """deal the hand"""
    card_is_used = []
    for index in range(0, 54):
        the_cards.append(index)
        card_is_used.append(False)

    the_hand = []
    for i in range(1, 54):
        card_is_used[i] = False

    for _ in range(5):
        a_card = randint(1, 52)
        while card_is_used[a_card]:
            a_card = randint(1, 52)
            # print("Card is used - pick another.")
        the_hand.append(a_card)
        card_is_used[a_card] = True
    # print(sorted(the_hand))
    return sorted(the_hand)


def print_and_rate_it(current_hand):
    print("\n")
    for item in range(5):
        print(find_card_face_string(current_hand[item]) + " of " + find_card_suit(current_hand[item]))
    print("")
    print(rate_the_hand(current_hand))


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


def convert_line_to_card(another_hand_from_file):
    new_hand = re.findall('\d+', another_hand_from_file)
    newer_hand = [int(new_hand[0]), int(new_hand[1]), int(new_hand[2]), int(new_hand[3]), int(new_hand[4])]
    return newer_hand


def build_hash_table():
    with open("possible_hand_list.txt", "r") as data_file:
        all_possible_hands = data_file.read().splitlines()
        data_file.close()
        with open("hash_table.txt", "w") as hash_file:
            for i in range(0, len(all_possible_hands)):
                aline = convert_line_to_card(all_possible_hands[i])
                sum1 = sum(aline)
                hash_file.write(f"{str(sum1)}\n")


def readin_hash_table():
    global hash_list
    with open("hash_table.txt", "r") as hash_file:
        hash_list = hash_file.read().splitlines()


#readin_hash_table()


def readin_all_hands():
    with open("possible_hand_list.txt", "r") as data_file:
        all_possible_hands = data_file.read().splitlines()
        data_file.close()
        return all_possible_hands


# the_index = hash_list.index("186")  1069 ther are 201 of them

#all_possible_hands = readin_all_hands()


# indices = []
# for i in range(len(hash_list)):
#     if str(sum(my_hand)) in hash_list[i]:
#         indices.append(i)
#
# print(f"the indices are {indices}")
# print(f"the length of indices is {len(indices)}")
#
# for i in range(len(indices)):
#     print(all_possible_hands[indices[i]])


###################################################
the_hand = []
my_hand = deal(the_hand)
print_and_rate_it(my_hand)
print("\n\n\n")


def discard_one(card_number):
    """ throw out the 'card numberth' card from my hand and see what happens"""
    global royal_flush_count, straight_flush_count, four_OAK_count, full_house_count, flush_count, straight_count, \
        three_OAK_count, two_pair_count, one_pair_count, high_card_count

    royal_flush_count = 0
    straight_flush_count = 0
    four_OAK_count = 0
    full_house_count = 0
    flush_count = 0
    straight_count = 0
    three_OAK_count = 0
    two_pair_count = 0
    one_pair_count = 0
    high_card_count = 0

    i_count = 0
    my_new_hand = my_hand.copy()

    for card in range(1, 53):
        if card not in my_hand:
            my_new_hand[card_number] = card
            if is_it_royal_flush(my_new_hand):
                royal_flush_count = + 1
            if is_it_a_straight(my_new_hand) and is_it_a_flush(my_new_hand):
                straight_flush_count += 1
            if is_it_4_of_a_kind(my_new_hand):
                four_OAK_count += 1
            if is_it_a_full_house(my_new_hand):
                full_house_count += 1
            if is_it_a_flush(my_new_hand):
                flush_count += 1
            if is_it_a_straight(my_new_hand):
                straight_count += 1
            if is_it_3_of_a_kind(my_new_hand):
                three_OAK_count += 1
            if is_it_2_pair(my_new_hand):
                two_pair_count += 1
            if is_it_a_pair(my_new_hand):
                high_card_count += 1

discard_one(0)
print(f"high_card probability = ", "%.2f" % (high_card_count/47*100), "%")
print(f"two_pair  probability = ", "%.2f" % (two_pair_count/47*100), "%")
print(f"three_OAK probability = ", "%.2f" % (three_OAK_count/47*100), "%")
print(f"straight probability = ", "%.2f" % (straight_count/47*100), "%")
print(f"flush probability = ", "%.2f" % (flush_count/47*100), "%")
print(f"full_house probability = ", "%.2f" % (full_house_count/47*100), "%")
print(f"four_OAK probability = ", "%.2f" % (four_OAK_count/47*100), "%")
print(f"straight_flush probability = ", "%.2f" % (straight_flush_count/47*100), "%")
print(f"royal_flush probability = ", "%.2f" % (royal_flush_count/47*100), "%")



