import yatzy as yz
import service

def user():
    var=int(input('How many players will play:'))
    all_players=dict()
    for x in range(1,var+1):
        players=input(f'Player {x}:')
        all_players[players]=empty_table()
    return all_players

def empty_table():
    return {
            'rolls': 0,
            'ones': '-',
            'twos': '-',
            'three': '-',
            'fours': '-',
            'fives': '-',
            'sixes': '-',
            'one pair': '-',
            'two pairs': '-',
            'three pairs': '-',
            'three of a kind': '-',
            'four of a kind':'-',
            'five of a kind': '-',
            'small straight': '-',
            'large straight': '-',
            'full straignt': '-',
            'full house': '-',
            'villa': '-',
            'towel': '-',
            'chance': '-',
            'maxi yatzy': '-'
            
            }


def main ():
    players = user()

    for r in range (20):
        for p in players:
            print('ROUND',r+1)
            rols = players[p]['rolls'] + 3 
            player, choice, var , rolls_player= yz.round({
                'player_name' : p,
                'rolls' : rols
            },
            players[p])

            players[p][choice] = var
            players[p]['rolls'] = rolls_player
    for c in players:
        print_table(c, players[c])
    print(players)

def final_tabel_for_user (player_name, tabel):
    bonus_points = service.sum_for_bonus(tabel)
    sum_points = service.sum_points_for_player(tabel)

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


def print_table(player_data):
    print(f"{'Category':<20} | {'Value':<10}")
    print('-' * 33)
    
    for key, value in player_data.items():
        print(f"{key:<20} | {value:<10}")
    
    print('-' * 33)

main()

""" test = {
    'rolls': 0, 'ones': 5, 'twos': 5, 'three': 5, 'fours': 5,
    'fives': 1, 'sixes': 2, 'one pair': 3, 'two pairs': 4,
    'three pairs': 5, 'three of a kind': 6, 'four of a kind': 7,
    'five of a kind': 8, 'small straight': 9, 'large straight': 10,
    'full straight': 11, 'full house': 12, 'villa': 13, 'towel': 14,
    'chance': 21, 'maxi yatzy': 15
}

print_table(final_tabel_for_user("pies", test)) """