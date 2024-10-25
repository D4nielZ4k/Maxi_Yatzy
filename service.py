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

    maxi_yatzy = combinations.chance(ls)

    return {
        'ones': ones,
        'twos': twos,
        'tres': tres,
        'fours': fours,
        'fives': fives,
        'sixes': sixes,
        'one_pair': one_pair,
        'two_pairs': two_pairs,
        'three_of_a_kind': three_of_a_kind,
        'four_of_a_kind': four_of_a_kind,
        'small_straight': small_straight,
        'large_straight': large_straight,
        'full_house': full_house,
        'chance': chance,
        'yatzy': maxi_yatzy
    }


def select_resoult(choice, ls):
    match choice:
        case 'ones':
           return results_for_round(ls)['ones']
        case 'twos':
           return results_for_round(ls)['twos']
        case 'tres':
           return results_for_round(ls)['tres']
        case 'fours':
           return results_for_round(ls)['fours']
        case 'fives':
           return results_for_round(ls)['fives']
        case 'sixes':
           return results_for_round(ls)['sixes']
        case 'sixes':
           return results_for_round(ls)['sixes']
       
        case 'one_pair':
           return results_for_round(ls)['one_pair']
        case 'two_pairs':
           return results_for_round(ls)['two_pairs']
        case 'three_of_a_kind':
           return results_for_round(ls)['three_of_a_kind']
        case 'small_straight':
           return results_for_round(ls)['small_straight']
        case 'big_straight':
           return results_for_round(ls)['large_straight']
        case 'full_house':
           return results_for_round(ls)['full_house']
        case 'chance':
           return results_for_round(ls)['chance']
        case 'yatzy':
           return results_for_round(ls)['yatzy']
       
def sum_for_bonus(player):
    ones = player['ones']
    twos = player['twos']
    tres = player['tres']
    fours = player['fours']
    fives = player['fives']
    sixes = player['sixes']
    return ones + twos + tres + fours + fives + sixes

def sum_points_for_player(player):
   bonus = 50 if sum_for_bonus(player) >= 63 else 0
   one_pair = player['one_pair']
   two_pairs = player['two_pairs']
   three_of_a_kind = player['three_of_a_kind']
   small_straight = player['small_straight']
   large_straight = player['large_straight']
   full_house = player['full_house']
   chance = player['chance']
   yatzy = player['yatzy']
   return bonus + one_pair + two_pairs + three_of_a_kind + small_straight + large_straight + full_house + chance + yatzy




#ls = [1,2,3,4,5,6]
#print(results_for_round(ls))