"""Poker aid main driver"""

import math
from random import randint

# to generate seed number
# seed(101)
# random number generation within 0 to 5

the_cards = []
card_is_used = []
all_possible_hands = []
a_hand = []

for index in range(1, 54):
    the_cards.append(index)
    card_is_used.append(False)

for index in range(1, 54):
    the_cards.append(index)
    card_is_used.append(False)


def count_values(this_hand, a_card):
    """looking for two, three, four of a kind"""
    count = 0
    for ele in this_hand:
        if find_card_value_int(ele) == find_card_value_int(a_card):
            count = count + 1
    return count


def is_it_a_straight(this_hand):
    """test for straight"""
    c_0 = int(find_card_value_int(this_hand[0]))
    c_1 = int(find_card_value_int(this_hand[1]))
    c_2 = int(find_card_value_int(this_hand[2]))
    c_3 = int(find_card_value_int(this_hand[3]))
    c_4 = int(find_card_value_int(this_hand[4]))
    if c_1 != c_0 + 1:
        return False
    if c_2 != c_1 + 1:
        return False
    if c_3 != c_2 + 1:
        return False
    if c_4 != c_3 + 1 and (c_4 != 1 and c_3 != 13):
        return False
    return True


def is_it_a_flush(this_hand):
    """test for flush"""
    c_0 = find_card_suit(this_hand[0])
    c_1 = find_card_suit(this_hand[1])
    c_2 = find_card_suit(this_hand[2])
    c_3 = find_card_suit(this_hand[3])
    c_4 = find_card_suit(this_hand[4])
    if c_0 == c_1 == c_2 == c_3 == c_4:
        return True
    else:
        return False


def is_it_royal(this_hand):
    """test for flush"""
    c_0 = int(find_card_value_int(this_hand[0]))
    c_1 = int(find_card_value_int(this_hand[1]))
    c_2 = int(find_card_value_int(this_hand[2]))
    c_3 = int(find_card_value_int(this_hand[3]))
    c_4 = int(find_card_value_int(this_hand[4]))
    if c_0 == 10 and c_1 == 11 and c_2 == 12 and c_3 == 13 and c_4 == 1:
        return True
    else:
        return False


def is_it_a_full_house(this_hand):
    """test for full house"""
    count_of_0 = count_values(this_hand, this_hand[0])
    count_of_1 = count_values(this_hand, this_hand[1])
    count_of_2 = count_values(this_hand, this_hand[2])
    count_of_3 = count_values(this_hand, this_hand[3])
    count_of_4 = count_values(this_hand, this_hand[4])

    if count_of_0 + count_of_1 + count_of_2 + count_of_3 + count_of_4 == 13:
        return True
    else:
        return False


def is_it_2_pair(this_hand):
    """test for 2 pair"""
    count_of_0 = count_values(this_hand, this_hand[0])
    count_of_1 = count_values(this_hand, this_hand[1])
    count_of_2 = count_values(this_hand, this_hand[2])
    count_of_3 = count_values(this_hand, this_hand[3])
    count_of_4 = count_values(this_hand, this_hand[4])

    if count_of_0 + count_of_1 + count_of_2 + count_of_3 + count_of_4 == 9:
        return True
    else:
        return False


def is_it_2_of_a_kind(this_hand):
    """test for a pair"""
    count_of_0 = count_values(this_hand, (this_hand[0]))
    count_of_1 = count_values(this_hand, (this_hand[1]))
    count_of_2 = count_values(this_hand, (this_hand[2]))
    count_of_3 = count_values(this_hand, (this_hand[3]))
    count_of_4 = count_values(this_hand, (this_hand[4]))
    half_way = False
    if count_of_0 + count_of_1 + count_of_2 + count_of_3 + count_of_4 == 7:
        return True
    else:
        return False


def is_it_3_of_a_kind(this_hand):
    """test for 3 of a kind"""
    count_of_0 = count_values(this_hand, (this_hand[0]))
    count_of_1 = count_values(this_hand, (this_hand[1]))
    count_of_2 = count_values(this_hand, (this_hand[2]))
    count_of_3 = count_values(this_hand, (this_hand[3]))
    count_of_4 = count_values(this_hand, (this_hand[4]))
    half_way = False
    if count_of_0 + count_of_1 + count_of_2 + count_of_3 + count_of_4 == 11:
        return True
    else:
        return False


def is_it_4_of_a_kind(this_hand):
    """test for 3 of a kind"""
    count_of_0 = count_values(this_hand, (this_hand[0]))
    count_of_1 = count_values(this_hand, (this_hand[1]))
    count_of_2 = count_values(this_hand, (this_hand[2]))
    count_of_3 = count_values(this_hand, (this_hand[3]))
    count_of_4 = count_values(this_hand, (this_hand[4]))
    half_way = False
    if count_of_0 + count_of_1 + count_of_2 + count_of_3 + count_of_4 == 17:
        return True
    else:
        return False


def rate_the_hand(the_hand):
    """hand rating"""
    if is_it_royal(the_hand) and is_it_a_flush(the_hand):
        return "royal flush"
    if is_it_a_straight(the_hand) and is_it_a_flush(the_hand):
        return "straight flush"
    if is_it_4_of_a_kind(the_hand):
        return "Four of a kind"
    if is_it_a_full_house(the_hand):
        return "full house"
    if is_it_a_flush(the_hand):
        return "flush"
    if is_it_a_straight(the_hand):
        return "straight"
    if is_it_3_of_a_kind(the_hand):
        return "Three of a kind"
    if is_it_2_pair(the_hand):
        return "Two Pair"
    if is_it_2_of_a_kind(the_hand):
        return "Two of a kind"

    values = []

    values.append(find_card_value_int(the_hand[0]))
    values.append(find_card_value_int(the_hand[1]))
    values.append(find_card_value_int(the_hand[2]))
    values.append(find_card_value_int(the_hand[3]))
    values.append(find_card_value_int(the_hand[4]))

    high_card = max(values)

    if find_card_value_int(min(values)) == 1:
        high_card = 1

    return f"{find_card_face_string(high_card)} High"


def deal(the_hand):
    """deal the hand"""
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


#  1-13 are spades A-K
# 14-26 are hearts
# 27-39 are diamonds
# 40-52 are clubs

def find_card_value_int(card_id):
    """find the integer value of cards"""
    value = card_id
    if value > 39:
        value = value - 13
    if value > 26:
        value = value - 13
    if value > 12:
        value = value - 13

    if card_id in (1, 14, 27, 40):
        value = 1
    if card_id in (11, 24, 37, 50):
        value = 11
    if card_id in (12, 25, 38, 51):
        value = 12
    if card_id in (13, 26, 39, 52):
        value = 13
    return value


def find_card_face_string(card_id):
    """find face value of a card"""
    face = card_id
    if face > 39:
        face = face - 13
    if face > 26:
        face = face - 13
    if face > 12:
        face = face - 13

    if card_id in (1, 14, 27, 40):
        face = "Ace"
    if card_id in (11, 24, 37, 50):
        face = "Jack"
    if card_id in (12, 25, 38, 51):
        face = "Queen"
    if card_id in (13, 26, 39, 52):
        face = "King"
    return str(face)


def find_card_suit(card_id):
    """find the suit of a card"""
    if 0 < card_id < 14:  # spades
        return "spades"
    if 13 < card_id < 27:  # hearts
        return "hearts"
    if 26 < card_id < 40:  # diamonds
        return "diamonds"
    if 39 < card_id < 53:  # clubs
        return "clubs"
    return "ERROR"


def combination(total_num, taken_at_a_time):
    """mathematical  combination calculation"""
    numerator = math.factorial(total_num)
    denominator = math.factorial(total_num - taken_at_a_time) * math.factorial(taken_at_a_time)
    return numerator / denominator


def probability(a_particular_hand):
    """probability calculations for a dealt hand"""
    number_of_possible_hands = combination(52, 5)
    if a_particular_hand == "royal flush":
        return 4 / number_of_possible_hands
    if a_particular_hand == "straight flush":
        return 40 / number_of_possible_hands
    if a_particular_hand == "4OAK":  # -- stands for 4 Of A Kind
        return combination(4, 4) * 13 * 48 / number_of_possible_hands
    if a_particular_hand == "full house":
        return 12 * 13 * combination(4, 2) * combination(4, 3) / number_of_possible_hands
    if a_particular_hand == "flush":
        return (4 * combination(13, 5) - 40) / number_of_possible_hands
    if a_particular_hand == "straight":
        return (10 * 4 ** 5 - 40) / number_of_possible_hands
    if a_particular_hand == "3OAK":
        return (13 * combination(4, 3) * (48 * 44) / 2) / number_of_possible_hands
    if a_particular_hand == "two pair":
        return (combination(13, 2) * combination(4, 2) ** 2 * 44) / number_of_possible_hands
    if a_particular_hand == "one pair":
        return 13 * combination(4, 2) * (48 * 44 * 40) / 6 / number_of_possible_hands
    if a_particular_hand == "high card":
        return (52 * 48 * 44 * 40 * 36 / 120 - 40 - 5108 - 10200) / number_of_possible_hands
    return 0


print(combination(52, 5))
# print("%.8f" % probability("royal flush"))
# print("%.8f" % probability("straight flush"))
# print("%.8f" % probability("4OAK"))
# print("%.8f" % probability("full house"))
# print("%.8f" % probability("flush"))
# print("%.8f" % probability("straight"))
# print("%.8f" % probability("3OAK"))
# print("%.8f" % probability("two pair"))
# print("%.8f" % probability("one pair"))
# print("%.8f" % probability("high card"))


# id = 25
# print(find_card_value(id) + " of " + find_card_face(id))


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

# all_possible_hands = all_hands_lister(all_possible_hands)

# this = sorted(all_possible_hands, key=lambda x:x[0])

# this = sorted(all_possible_hands, key = lambda x: x[2])
# this = sorted(this, key = lambda x: x[1])

# s = sorted(all_possible_hands)


# for i in range(0, len(s)):
#     sum = s[i][0] + s[i][1] + s[i][2] + s[i][3] + s[i][4]
#     print(s[i])
#     # print(" and the sum is      " + str(sum))


# def write_list_to_file(s):
#     with open("possible_hand_list.txt", "w") as f_for_writing:
#         for i in range(0, len(s)):
#             the_thing = str(s[i]) + "\n"
#             f_for_writing.write(str(i + 1) + ": " + the_thing)

# write_list_to_file(s)
