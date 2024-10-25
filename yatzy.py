import service

player_1 = {'player_name': 'name',
            'rolls' : 3
            }


def round (player):
    p = player
    final_dices = []
    while player["rolls"]  != 0 :
        p["rolls"] = p["rolls"] - 1
        dices = service.dice_roll(6 - len(final_dices))

        print("you table " , final_dices)
        print(dices)
        player_choice_for_roll = int(input("1 wybierz kosci czy wybierz z tabeli wynik"))
        
        print(service.results_for_round(final_dices +dices))
        
        if player_choice_for_roll == 2:
            player["rolls"] = player["rolls"] - 1


        if player_choice_for_roll == 0:
            final_dices = dices + final_dices
            print(final_dices)
            return (p, final_dices)
        if player_choice_for_roll == 1:
            while len(dices) > 0:
                print("you table " , final_dices)

                l = len(dices)
                print(f'wybierz miedzy 0 - {l-1}'+ ' dla losowania reszty - 1 a dla wyboru wyniku ')
                
                print(dices)
                user_choice = int(input("wybierz kosc do zachowania"))

                if user_choice == -1:
                    break

                final_dices += [dices[user_choice]]
                dices.pop(user_choice)
                
               

                
    return player, final_dices





print(round(player_1))
