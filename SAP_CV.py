import pyautogui as pag
import sys
import os
import time
"""

"""

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

def identify_shop(tl_list):
    """
    takes a list of the top left coordinates for each shop slot
    runs the identify function over all shop slots.
    returns a dictionary of shop slots: animal/food
    """
    shop = {}
    for i, tl_coords in enumerate(tl_list):

        if i < 5:
            shop[f'slot_{i}'] = identify_pet(tl_coords)
        else:
            shop[f'slot_{i}'] = identify_food(tl_coords)
    return shop
if __name__ == '__main__':


    slot_coords = [(450, 630), (590, 630), (740, 630), (890, 630), (1025, 630), (1175, 630), (1325, 630)]
    team_coords = [(450, 350), (590, 350), (740, 350), (890, 350), (1025, 350)]

    team = [None, None, None, None, None]

    shop = identify_shop(slot_coords)
    print('{}|{}|{}|{}|{}|{}|{}|'.format(*shop.values()))
