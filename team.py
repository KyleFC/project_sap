class Team:
    #team_dict is a dictionary of strings representing animals but should be a
    #dictionary of pet classes in the future
    def __init__(self, team_dictionary,):
        self.team_dict = team_dictionary
        self.team_coords = [(450, 350), (590, 350), (740, 350), (890, 350), (1025, 350)]

    def print_team(self):
        """
        print a formatted representation of the animals on the team.
        """
        print("{}|{}|{}|{}|{}".format(*self.team_dict.values()))
if __name__ == '__main__':
    pass
