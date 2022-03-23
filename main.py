import pet
import shop
import team
import game
import SAP_CV
import events

if __name__ == '__main__':
    shop_dict = {'slot_0': None, 'slot_1': None, 'slot_2': None, 'slot_3': None, 'slot_4': None, 'slot_5': None, 'slot_6': None}
    my_shop = shop.Shop(shop_dict)

    team_dict = {'slot_0': None, 'slot_1': None, 'slot_2': None, 'slot_3': None, 'slot_4': None}
    sample_team = team.Team(team_dict)

    game = game.Game(my_shop, sample_team, 10, 1, 15)
    game.shop.update()
    game.print_game()
    game.buy(0, 4)
    game.buy(0, 3)
    game.buy(0, 2)
    game.roll()
    game.end_turn()
    time.sleep(2)
    game.pick_name()
    game.end_turn()
