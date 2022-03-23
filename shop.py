import SAP_CV

class Shop:
    #might need to add some variables to the init at some point (round?)
    def __init__(self, shop_dictionary = {}, team_dictionary = {}, cans=0):
        self.shop_coords = [(450, 630), (590, 630), (740, 630), (890, 630), (1025, 630), (1175, 630), (1325, 630)]
        self.team_coords = [(450, 350), (590, 350), (740, 350), (890, 350), (1025, 350)]
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
                self.shop_dict[f'slot_{i}'] = SAP_CV.identify_pet(tl_coords)
            else:
                self.shop_dict[f'slot_{i}'] = SAP_CV.identify_food(tl_coords)

        print('shop has been updated')
if __name__ == '__main__':
    pass
