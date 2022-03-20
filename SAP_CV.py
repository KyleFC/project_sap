import pyautogui as pag
import sys
import os
import time

class Shop:
    #might need to add some variables to the init at some point (tier?)
    def __init__(self, shop_coordinates, team_coordinates, shop_dictionary = {}, team_dictionary = {}):
        self.shop_coords = shop_coordinates
        self.team_coords = team_coordinates
        self.shop_dict = shop_dictionary
        self.team_dict = team_dictionary

    def print_shop(self):
        """
        print a formatted representation of the animals/food in every shop slot.
        """
        print("{}|{}|{}|{}|{}|{}|{}".format(*self.shop_dict.values()))

    def get_shop_coords(self):
        """
        return shop slot coordinates as a list
        """
        return self.shop_coords

    def get_team_coords(self):
        """
        return team slot coordinates as a list
        """
        return self.team_coords

    def update(self):
        """
        takes a list of the top left coordinates for each shop slot
        runs the identify function over all shop slots.
        returns a dictionary of shop slots: animal/food or None
        """
        for i, tl_coords in enumerate(self.shop_coords):

            if i < 5:
                self.shop_dict[f'slot_{i}'] = identify_pet(tl_coords)
            else:
                self.shop_dict[f'slot_{i}'] = identify_food(tl_coords)
        print('shop has been updated')

class Team:
    #team_dict is a dictionary of strings representing animals but should be a
    #dictionary of pet classes in the future
    def __init__(self, team_dictionary, team_coordinates):
        self.team_dict = team_dictionary
        #maybe add the +50 to x and y here eventually if i know i'm not doing any cv stuff here
        self.team_coords = team_coordinates

    def print_team(self):
        """
        print a formatted representation of the animals on the team.
        """
        print("{}|{}|{}|{}|{}".format(*self.team_dict.values()))

class Game:

    def __init__(self, shop, team, gold, round, hearts):
        self.shop = shop
        self.team = team
        self.gold = gold
        self.round = round
        self.hearts = hearts

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

    def buy(self, item, shop_slot, team_slot):
        """
        buys the pet or food in shop_slot __. 0 - 6
        puts the pet/food on team_slot
        adds the animal
        """
        pag.moveTo(self.shop_coords[shop_slot][0] + 50, self.shop_coords[shop_slot][1] + 50)
        time.sleep(.1)
        pag.click()
        time.sleep(.5)
        pag.moveTo(self.team_coords[team_slot][0] + 50, self.team_coords[team_slot][1] + 50)
        time.sleep(.5)
        pag.click()
        
    def roll(self):
        """
        Reroll the shop
        """
        pag.moveTo(200, 950)
        time.sleep(.1)
        pag.click()

    def end_turn(self):
        """
        End turn. Assumes gold is 0.
        """
        pag.moveTo(1700, 950)
        time.sleep(.1)
        pag.click()

    def print_game(self):
        self.shop.print_shop()
        self.team.print_team()

def identify_pet(top_left):
    """
    Uses the top left coordinate of a shop or team slot to identify a pet.
    lower tier pets get searched first.
    returns the name of the pet or None if it isn't found.
    """
    for filename in os.listdir('pets'):
        f = os.path.join('pets', filename)

        found_pet = pag.locateOnScreen(f, grayscale=True, confidence=.7, region=(top_left[0], top_left[1], 150, 150))

        if found_pet != None:
            pet_name = filename[1:-4]
            if pet_name == 'empty':
                return None
            return pet_name
    return None

def identify_food(top_left):
    """
    Uses the top left coordinate of a shop slot to identify food.
    lower tier food gets searched first.
    returns the name of the food or None if it isn't found.
    """
    found_food = None
    for filename in os.listdir('food'):
        f = os.path.join('food', filename)

        found_food = pag.locateOnScreen(f, grayscale=True, confidence=.7, region=(top_left[0], top_left[1], 150, 150))

        if found_food != None:
            food_name = filename[1:-4]
            if food_name == 'empty':
                return None
            return food_name

    return None



if __name__ == '__main__':


    slot_coords = [(450, 630), (590, 630), (740, 630), (890, 630), (1025, 630), (1175, 630), (1325, 630)]
    team_coords = [(450, 350), (590, 350), (740, 350), (890, 350), (1025, 350)]

    team = [None, None, None, None, None]
    res = pag.size()
    if res != (1920, 1080):
        print('not 1920x1080')


######################TEST ZONE#################################
    shop_dict = {'slot_0': 'pig', 'slot_1': 'ant', 'slot_2': 'duck', 'slot_3': None, 'slot_4': None, 'slot_5': None, 'slot_6': 'apple'}
    my_shop = Shop(slot_coords, team_coords, shop_dict)
    team_dict = {'slot_0': 'pig', 'slot_1': 'ant', 'slot_2': 'duck', 'slot_3': 'swan', 'slot_4': 'fish'}
    sample_team = Team(team_dict, team_coords)
    """time.sleep(2)
    coords = my_shop.get_shop_coords()
    my_shop.update()
    my_shop.print_shop()
    time.sleep(2)
    my_shop.roll()
    time.sleep(2)
    my_shop.buy(2, 0)
    time.sleep(2)
    my_shop.buy(1, 1)
    time.sleep(2)
    my_shop.buy(0, 2)
    time.sleep(1)
    my_shop.end_turn()
"""
    game = Game(my_shop, sample_team, 10, 1, 15)
    game.print_game()
    game.move(0, 4)
    game.print_game()
