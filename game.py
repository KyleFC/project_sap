import shop
import pet
import team

class Game:

    def __init__(self, shop, team, gold, round, hearts):
        self.shop = shop
        self.team = team
        self.gold = gold
        self.round = round
        self.hearts = hearts

    def pick_name(self):
        #should change to pick_name(self, option1, option2)?
        """
        pick a random name
        """
        name_coords = [(400, 400), (1000, 400), (1500, 400), (400, 700), (1000, 700), (1500, 700)]
        n1 = random.choice(name_coords[:3])
        n2 = random.choice(name_coords[3:])
        pag.moveTo(n1)
        time.sleep(.1)
        pag.click()
        time.sleep(.1)
        pag.moveTo(n2)
        time.sleep(.1)
        pag.click()
        time.sleep(1)

    def move(self, slot1, slot2, click=False):
        """
        move a pet from slot_? to slot_?
        if the pets are the same then it will combine
        """
        slot_coords_1 = self.shop.team_coords[slot1][0] + 50, self.shop.team_coords[slot1][1] + 50
        slot_coords_2 = self.shop.team_coords[slot2][0] +50, self.shop.team_coords[slot2][1] + 50
        dist = slot1 - slot2
        if click:
            pag.moveTo(slot_coords_1)
            time.sleep(.1)
            pag.click()
            time.sleep(.5)
            pag.moveTo(slot_coords_2)
            time.sleep(.1)
            pag.click()
            time.sleep(1)

        #inner team logic
        pet = self.team.team_dict[f'slot_{slot1}']
        print(f'moving {slot1} to {slot2}')
        self.team.team_dict[f'slot_{slot1}'] = None

        if self.team.team_dict[f'slot_{slot2}'] == None or abs(dist) == 1:
            self.team.team_dict[f'slot_{slot1}'] = self.team.team_dict[f'slot_{slot2}']
            self.team.team_dict[f'slot_{slot2}'] = pet

        #move from right to left. pets get pushed forward from slot
        elif dist > 0:
            for i in range(dist):
                self.team.team_dict[f'slot_{slot1-i}'] = self.team.team_dict[f'slot_{slot1-i-1}']
                #print(f'pushing {slot1-i-1} to {slot1-i}')
            self.team.team_dict[f'slot_{slot2}'] = pet

        #move from left to right. pets get pushed backwards from slot
        else:
            for i in range(-dist):
                self.team.team_dict[f'slot_{slot1+i}'] = self.team.team_dict[f'slot_{slot1+i+1}']
                #print(f'pushing {slot1+i} to {slot1+i+1}')
            self.team.team_dict[f'slot_{slot2}'] = pet

    def buy(self, shop_slot, team_slot):
        """
        buys the pet or food in shop_slot __. 0 - 6
        puts the pet/food on team_slot
        adds the animal
        """
        pag.moveTo(self.shop.shop_coords[shop_slot][0] + 50, self.shop.shop_coords[shop_slot][1] + 50)
        time.sleep(.1)
        pag.click()
        time.sleep(.5)
        pag.moveTo(self.shop.team_coords[team_slot][0] + 50, self.shop.team_coords[team_slot][1] + 50)
        time.sleep(.5)
        pag.click()
        self.gold -= 3
        print(f'bought {self.shop.shop_dict[f"slot_{shop_slot}"]} and put it in slot {team_slot}')
        if shop_slot < 5:
            for i in range(5 - shop_slot):
                self.shop.shop_dict[f'slot_{shop_slot}'] = self.shop.shop_dict[f'slot_{shop_slot+1}']
        self.team.team_dict[f'slot_{team_slot}'] = self.shop.shop_dict[f'slot_{shop_slot}']
        time.sleep(1)

    def sell(self, slot):
        #once a pet class is implemented this will add the correct amount of gold
        """
        sell the pet in slot_?
        """
        pag.moveTo(self.team.team_slot[slot][0] + 50, self.team.team_slot[slot][1])
        time.sleep(.1)
        pag.click()
        time.sleep(.1)
        pag.moveTo(1000, 950)
        time.sleep(.1)
        pag.click()
        time.sleep(1)
        print(f'sold {self.team.team_dict[f"slot_{slot}"]} in slot {slot}')
        self.team.team_dict[f'slot_{slot}'] = None

    def roll(self):
        """
        Reroll the shop
        """
        pag.moveTo(200, 950)
        time.sleep(.1)
        pag.click()
        self.gold -= 1
        print(f'rerolled the shop')
        time.sleep(1)

    def end_turn(self):
        """
        End turn. Assumes gold is 0.
        """
        pag.moveTo(1700, 950)
        time.sleep(.1)
        pag.click()
        print(f'ending turn')

    def print_game(self):
        """
        Print shop and team information
        """
        self.shop.print_shop()
        self.team.print_team()
        
if __name__ == '__main__':
    pass
