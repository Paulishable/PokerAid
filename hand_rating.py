from card_utilities import *


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


def is_it_a_pair(this_hand):
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

def keep_the_hand(the_hand):
    """add the hand to the possible list if it is at least 2 pair"""
    if is_it_royal(the_hand) and is_it_a_flush(the_hand):
        return True
    if is_it_a_straight(the_hand) and is_it_a_flush(the_hand):
        return True
    if is_it_4_of_a_kind(the_hand):
        return True
    if is_it_a_full_house(the_hand):
        return True
    if is_it_a_flush(the_hand):
        return True
    if is_it_a_straight(the_hand):
        return True
    if is_it_3_of_a_kind(the_hand):
        return True
    if is_it_2_pair(the_hand):
        return True
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
    if is_it_a_pair(the_hand):
        return "You have 1 pair"

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
