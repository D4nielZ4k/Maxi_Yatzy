import random
import combinations

def dice_roll(dices_value):
    rolls = []
    for i in range(dices_value):
        rolls.append(random.randint(1,6))
    return rolls

def results_for_round(ls):
    
    ones = combinations.ones_sixes(ls, 1)

    twos = combinations.ones_sixes(ls, 2)

    tres = combinations.ones_sixes(ls, 3)

    fours = combinations.ones_sixes(ls, 4)

    fives = combinations.ones_sixes(ls, 5)

    sixes = combinations.ones_sixes(ls, 6)

    one_pair = combinations.one_pair(ls)

    two_pairs = combinations.two_pair(ls)

    three_pair = combinations.three_pair(ls)

    three_of_a_kind = combinations.three_of_a_kind(ls)

    four_of_a_kind = combinations.four_of_a_kind(ls)

    five_of_a_kind = combinations.three_of_a_kind(ls)

    small_straight = combinations.smal_straight(ls)

    large_straight = combinations.large_straight(ls)

    full_straight = combinations.large_straight(ls)

    full_house = combinations.full_house(ls)

    villa = combinations.villa(ls)

    towel = combinations.towel(ls)

    chance = combinations.chance(ls)

    maxi_yatzy = combinations.maxi_yatzy(ls)

    return {
        'ones': ones,
        'twos': twos,
        'three': tres,
        'fours': fours,
        'fives': fives,
        'sixes': sixes,
        'one pair': one_pair,
        'two pairs': two_pairs,
        'three pairs': three_pair,
        'three of a kind': three_of_a_kind,
        'four of a kind': four_of_a_kind,
        'five of a kind': five_of_a_kind,
        'small straight': small_straight,
        'large straight': large_straight,
        'full straignt': full_straight,
        'full house': full_house,
        'villa' :villa,
        'towel' : towel,
        'chance': chance,
        'maxi yatzy': maxi_yatzy
    }


       
def sum_for_bonus(player):
    ones = player['ones']
    twos = player['twos']
    tres = player['three']
    fours = player['fours']
    fives = player['fives']
    sixes = player['sixes']
    return ones + twos + tres + fours + fives + sixes

def sum_points_for_player(player):
   bonus = 50 if sum_for_bonus(player) >= 63 else 0
   
   one_pair = player['one pair']
   two_pairs = player['two pairs']
   three_pair = player['three pairs']
   three_of_a_kind = player['three of a kind']
   four_of_a_kind = player['four of a kind']
   five_of_a_kind = player['five of a kind']
   small_straight = player['small straight']
   large_straight = player['large straight']
   full_straight = player['full straight']
   full_house = player['full house']
   villa = player['villa']
   towel = player['towel']
   chance = player['chance']
   maxi_yatzy = player['maxi yatzy']

   return (bonus + one_pair + two_pairs + three_pair + three_of_a_kind + four_of_a_kind + five_of_a_kind+
            + small_straight + large_straight + full_straight + 
            full_house + villa + towel + chance + maxi_yatzy)

""" player1 = {
    'rolls': 0,
    'ones': 0,
    'twos': 1,
    'three': 3,
    'fours': 1230,
    'fives': 21,
    'sixes': 1,
    'one pair': 0,
    'two pairs': 0,
    'three pairs': 0,
    'three of a kind': 0,
    'four of a kind': 0,
    'five of a kind': 0,
    'small straight': 23,
    'large straight': 123,
    'full straight': 0,
    'full house': 23,
    'villa': 123,
    'towel': 0,
    'chance': 0,
    'maxi yatzy': 0
}

print(sum_points_for_player(player1)) """