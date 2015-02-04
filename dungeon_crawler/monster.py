class Monster(object):

    def __init__(self):
        self.name = "Fluffy"
        self.health = 100
        self.hit_points = 10

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_hit_points(self):
        return self.hit_points

    def take_hit(self, hit):
        self.health = self.health - hit

    def get_status(self):
        print "Monster's health is: " + str(self.get_health())


class Fluffy(Monster):
    def __init__(self, player_health, player_hit_points):
        Monster.__init__(self)
        self.name = "Fluffy"
        self.health = player_health * 1.2
        self.hit_points = player_hit_points * .4


class Ghost(Monster):
    def __init__(self, player_health, player_hit_points):
        Monster.__init__(self)
        self.name = "Ghost"
        self.health = player_health * 1.4
        self.hit_points = player_hit_points * .6


class Clown(Monster):
    def __init__(self, player_health, player_hit_points):
        Monster.__init__(self)
        self.name = "Clown"
        self.health = player_health * 1.6
        self.hit_points = player_hit_points * .8
