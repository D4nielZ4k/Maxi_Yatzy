import random
import combinations


#function does what its name indicates
def dice_roll(dices_value):
    rolls = []
    for i in range(dices_value):
        rolls.append(random.randint(1,6))
    return rolls
#function does what its name indicates
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

    five_of_a_kind = combinations.five_of_a_kind(ls)

    small_straight = combinations.smal_straight(ls)

    large_straight = combinations.large_straight(ls)

    full_straight = combinations.full_straight(ls)

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
        'full straight': full_straight,
        'full house': full_house,
        'villa' :villa,
        'towel' : towel,
        'chance': chance,
        'maxi yatzy': maxi_yatzy
    }



#function does what its name indicates    
def sum_for_bonus(player):
    ones = player['ones']
    twos = player['twos']
    tres = player['three']
    fours = player['fours']
    fives = player['fives']
    sixes = player['sixes']
    return ones + twos + tres + fours + fives + sixes


#function does what its name indicates
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


#function does what its name indicates
def get_int_tabel(tabel):
    output_table = {}

    for key, value in tabel.items():
        if isinstance(value, int):
            output_table[key] = value 
        else:
            output_table[key] = 0

    return output_table

#function does what its name indicates
def print_table(player_data):
    print(f"{'Category':<20} | {'Value':<10}")
    print('-' * 33)
    
    for key, value in player_data.items():
        print(f"{key:<20} | {value:<10}")
    
    print('-' * 33)

#function does what its name indicates
def final_tabel_for_user (player_name, player_tabel):
    tabel = get_int_tabel(player_tabel)
    bonus_points = sum_for_bonus(tabel)
    sum_points = sum_points_for_player(tabel)

    bonus = 50 if bonus_points >= 63 else 0
    
    fin = {'Player name' : player_name,
            'ones': tabel['ones'],
            'twos': tabel['twos'],
            'three': tabel['three'],
            'fours': tabel['fours'],
            'fives': tabel['fives'],
            'sixes': tabel['sixes'],
            'sum': bonus_points,
            'Bonus (63+)' : bonus,
            'one pair': tabel['one pair'],
            'two pairs': tabel['two pairs'],
            'three pairs': tabel['three pairs'],
            'three of a kind': tabel['three of a kind'],
            'four of a kind':tabel['four of a kind'],
            'five of a kind': tabel['five of a kind'],
            'small straight': tabel['small straight'],
            'large straight': tabel['large straight'],
            'full straight': tabel['full straight'],
            'full house': tabel['full house'],
            'villa': tabel['villa'],
            'towel': tabel['towel'],
            'chance': tabel['chance'],
            'maxi yatzy': tabel['maxi yatzy'],
            'TOTAL SUM': sum_points
           }
    return fin