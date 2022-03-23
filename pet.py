import events

class Pet:
    #set up events and add them here
    def __init__(self, name, attack, health, level, ability=None):
        self.name = name
        self.attack = attack
        self.health = health
        self.ability = ability
        self.level = level
        self.events = events.Event()

    def add_stats(self, attack = 0, health = 0):
        """
        adds attack or health to pet. can also be used to subtract health for effects like cupcake with temporary buffs.
        """
        self.attack = min(attack + self.attack, 50)
        self.health = min(health + self.health, 50)

    def add_level(self, xp):
        """
        add experience to pet.
        """
        if xp < 6:
            self.level += xp
        else:
            print('Attempting to level max level pet')

    def add_event(self, event_func):
        self.events += event_func

if __name__ == '__main__':
    pass
