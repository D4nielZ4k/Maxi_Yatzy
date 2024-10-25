import service

player_1 = {'ones': 0,
            'twos': 64,
            'tres': 0,
            'fours': 0,
            'fives': 0,
            'sixes': 0,
            'one_pair': 0,
            'two_pairs': 1,
            'three_of_a_kind': 43,
            'small_straight': 12,
            'large_straight': 25,
            'full_house': 0,
            'chance': 0,
            'yatzy': 66}

print(service.sum_points_for_player(player_1))