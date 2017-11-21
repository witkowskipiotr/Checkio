from models.casino import Casino

casino = Casino(name='Cristal Casino', adress='Królewska 11, Warszawa')

gregor = casino.add_croupier(name='Grzegorz', surname='Brzęczyszczykiewicz', shuffle_last=True)

mike = casino.add_player(name='Michał', surname='Nowak', money=10, type_player='random')
peter = casino.add_player(name='Piotr', surname='Witkowski', money=100.52, type_player='random')
lukas = casino.add_player(name='Łukasz', surname='Witkowski', money=12, type_player='random')
arthur = casino.add_player(name='Artur', surname='Witkowski', money=1000, type_player='random')

table_green = casino.add_table(name='Green', max_number_of_players=4)


def check_who_left_game(game):
    for player in game.game_players:
        if player.when_finish_game == game.step:
            print(player.name, player.surname, "left game before end.")


def get_info_players(game):
    print("Cards on the table:", game.cards_on_table)
    for player in game.game_players:
        print("Cards", player.name, player.surname,": ", player.cards )
        print(game.best_combination_card_layout(player=player))
        print()


def start_game(game):
    game.start_game()
    game.preflop_round()
    get_info_players(game=game)
    print("Pre flop round:")
    step = input("Please click enter to flop round")
    game.step = 2
    check_who_left_game(game=game)
    win = game.flop_round()
    get_info_players(game=game)
    if win and isinstance(win, bool):
        step = input("Please click enter to turn round")
        game.step = 3
        check_who_left_game(game=game)
        win = game.turn_round()
        get_info_players(game=game)
    if win and isinstance(win, bool):
        step = input("Please click enterto river round")
        game.step = 4
        check_who_left_game(game=game)
        win = game.river_round()
        get_info_players(game=game)
    if win and isinstance(win, bool):
        win = game.who_win()
    if win and not isinstance(win, bool):
        print("The winner is:")
        print(win.name, win.surname)
        print(game.best_combination_card_layout(player=win))


repeat = True
while repeat:
    number_players = input("Amount players between 2 and 4: \n")
    try:
        numbers = int(number_players)
        if numbers in [2, 3, 4]:
            for number, player in zip (range(numbers), casino.players):
                print(number, player.name, player.surname)
                casino.add_player_to_table(name_table="Green", player=player)

            repeat_start_game = True
            while repeat_start_game:
                repeat_get_money = True
                while repeat_get_money:
                    money_min_to_connect = input("how much does it cost to connect to the game: \n")
                    try:
                        money_min_to_connect = int(money_min_to_connect)
                        repeat_get_money = False
                    except:
                        print("Please take integer, not string")

                game = casino.create_game_omaha(table_name="Green", croupier=gregor,
                                                money_min_to_connect=money_min_to_connect)
                if not game:
                    chose_y_n = input("Do you want to change your bid? (y/n): \n")
                    if chose_y_n not in ['Y', 'y']:
                        repeat_start_game = False
                else:
                    repeat_start_game = False
                    print("Create game, players in game:")
                    for player in game.game_players:
                        print(player.name, player.surname)
                    start_game(game=game)
                    repeat = False

            repeat = False
        else:
            print("Numbers of players is not in 2, 3, 4")

    except:
        print("Please take integer, not string")

