import service


def round (player, tabel):
    p = player
    player_name = p['player_name']


    final_dices = []
    while player["rolls"]  > 0 :
       
        print("Player's turn : ___" , player_name," _____")
        print("you have !!!!!!!!!!!!! ",player["rolls"] , "rolls to use" )
        p["rolls"] = p["rolls"] - 1
        rolls_for_player = p["rolls"]
        
        
        dices = service.dice_roll(6 - len(final_dices))
        if len(dices) == 0:
            break

        possibilities = print_possibilities(final_dices + dices, tabel)
        
        print("you table " , final_dices)
        print(dices)
        
       
       
        player_choice_for_roll = get_valid_user_choice()
        #DZIALA ZAJEBIOZA 
        if player_choice_for_roll == 2:
            return final_choice(possibilities, player_name, rolls_for_player)
        
        if player_choice_for_roll == 3:
            if player["rolls"]  == 0:
                return final_choice(possibilities,player_name, rolls_for_player)
            else:
                continue
       
        if player_choice_for_roll == 1:
            while len(dices) > 0 :
                print("Your dice:", final_dices)
                l = len(dices)
                print(f'Choose between 1 and {l} (or -1 to finish selection):')
                print("Available dice:")
                for idx, die in enumerate(dices, start=1):
                    print(f"{idx}: {die}")

                try:
                    user_choice = int(input("Choose a die to keep: "))
                except ValueError:
                    print("Invalid choice. Please enter an integer.")
                    continue
                
                if user_choice == -1:
                    break
                if 1 <= user_choice <= len(dices):
                    final_dices.append(dices[user_choice - 1])
                    dices.pop(user_choice - 1)
                
                else:
                    print("Choice out of range. Please try again.")
    print(final_dices)
    print_possibilities(final_dices,tabel)
    return final_choice(possibilities,player_name, rolls_for_player)
                
        
def final_choice(possibilities, player_name, rolss_left):
    while True:
                choice = input("Write your choice: ")
                if choice in possibilities:
                    print(possibilities[choice])
                    return player_name, choice, possibilities[choice],rolss_left
                else:
                    print("Invalid choice. Please enter one of the valid options:", ", ".join(possibilities.keys()))




def print_possibilities(ls, player_table):
    data = service.results_for_round(ls)
    data = {
        key: value
        for key, value in data.items()
        if value != 0 and not (key in player_table and player_table[key] != '-')
    }
    
    if data:
        print(f"{'Category':<20} {'Value':<10}")
        print('-' * 30)
        for key, value in data.items():
            print(f"{key:<20} {value:<10}")
        
        print('_' * 30)
        
        return data
    else:
       
        data_for_no_possi = {}
        for i in player_table:
            if player_table[i] == '-':
                data_for_no_possi[i] = 0 
        print('-' * 30)
        print('Unfortunately you have to choose something from the table!')
        print('-' * 30)
        print(f"{'Category':<20} {'Value':<10}")
        print('-' * 30)
        for key, value in data_for_no_possi.items():
            print(f"{key:<20} {value:<10}")
        
        print('_' * 30)
        
        return data_for_no_possi

def get_valid_user_choice():
    valid_options = [1, 2, 3]
    while True:
        user_input = input(
            "Choose an option:\n"
            "1. Choose dice to add to your table\n"
            "2. Select the category to save your result\n"
            "3. Roll the remaining dice\n"
            "Your choice: "
        )
        try:
            choice = int(user_input)
            if choice in valid_options:
                return choice
            else:
                print("Invalid choice. Please enter one of the following options: 1, 2, 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


""" h = {       'rolls': 0,
            'ones': 1,
            'twos': 1,
            'three': 1,
            'fours': 1,
            'fives': 1,
            'sixes': 1,
            'one pair': 1,
            'two pairs': 1,
            'three pairs': '-',
            'three of a kind': 1,
            'four of a kind':1,
            'five of a kind': 1,
            'small straight': '-',
            'large straight': '-',
            'full straignt': '-',
            'full house': '-',
            'villa': '-',
            'towel': '-',
            'chance': 1,
            'maxi yatzy': 1}

l = [1 ,2 , 3, 4 ,1 , 1]
print_possibilities(l,h ) """