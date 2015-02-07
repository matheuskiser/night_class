import os


class Player():
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.hit_points = 20

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_hit_points(self):
        return self.hit_points

    def display_player_config(self):
        print "Player's Status:"
        print "Level: " + str(self.get_level())
        print "Health: " + str(self.get_health())
        print "Hit Points: " + str(self.get_hit_points())

    def take_hit(self, hit, monster_name):
        self.health = self.health - hit
        print monster_name + " just attacked you."

    def get_status(self):
        if self.get_health() > 0:
            print "Your health is: " + str(self.get_health())

    def get_level(self):
        return self.level

    def raise_level(self):
        # Raises level by 1
        self.level += 1

        # Increases hit_points by 2
        self.hit_points += 1

        # Wipes screen from previous level
        os.system('clear')

        # Levels up
        if self.get_level() <= 3:
            print "Congratulations! You have leveled up!"
            print "Your current level is " + str(self.get_level())

            # Displays player's status when player has leveled up
            self.display_player_config()
        else:
            print "You have killed all of the monsters!\n"