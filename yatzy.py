import service

player_1 = {'player_name': 'name',
            'rolls' : 3
            }


def round (player):
    p = player

    key = ""
    value = 0

    final_dices = []
    while player["rolls"]  > 0 :
        p["rolls"] = p["rolls"] - 1
        dices = service.dice_roll(6 - len(final_dices))


        #USUNAC TE KTORE SA JUZ WYBRANE 
        possibilities = print_possibilities(final_dices + dices)
        
        print("you table " , final_dices)
        print(dices)
        
       
       
        player_choice_for_roll = int(input("1 choice dicev to you table, \n2 write wich type you will save to you result \n"))
        #DZIALA ZAJEBIOZA 
        if player_choice_for_roll == 2:
            while True:
                choice = input("Write your choice: ")
                if choice in possibilities:
                    print(possibilities[choice])
                    return p, choice, possibilities[choice]
                else:
                    print("Invalid choice. Please enter one of the valid options:", ", ".join(possibilities.keys()))

        #DZIALA ZAJEBIOZA
        if player_choice_for_roll == 0:
            print(final_dices)
            while True:
                choice = input("Write your choice: ")
                if choice in possibilities:
                    print(possibilities[choice])
                    return p, choice, possibilities[choice]
                else:
                    print("Invalid choice. Please enter one of the valid options:", ", ".join(possibilities.keys()))

                
        if player_choice_for_roll == 1:
            while len(dices) > 0:
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


#RETUNR player name , key for example "CHANE ", and  value for expaple " 11"



def print_possibilities(ls):
    
    data = service.results_for_round(ls)

    data = {key: value for key, value in data.items() if value != 0}
    
    if len(data) > 0:
        print(f"{'Category':<20} {'Value':<10}")
        print('-' * 30)
        for key, value in data.items():
            print(f"{key:<20} {value:<10}")
        
        c = "_"
        print(f'{c}' * 30)
        
        return data
    else:
        print("No possibilities")   


round(player_1)