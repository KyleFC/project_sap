import pyautogui as pag
import sys
import os
import time
import random

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
    print(identify_pet(450, 630)) #first shop pet
    print(identify_food(1325, 630)) #last shop food
