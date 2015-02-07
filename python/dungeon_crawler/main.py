from player import Player
from monster import *
import random


# Displays to player what they want to do
def display_menu():
    option = 0

    while option != 2:
        print "1. Start a game"
        print "2. Exit"
        option = int(raw_input("Pick an item: "))
        pick_option(option)


# Picks option from what user picked
def pick_option(option):
    if option == 1:
        # Start game
        start_game()
    elif option == 2:
        # Exit program
        print "Thanks for playing!\n"


# If random number comes to be even, then monster attacks
def random_monster_attack(player, monster):
    rand_number = random.randint(0, 100)

    if monster.get_health() > 0:
        # Monster attacks player if rand_number is even
        if rand_number % 2 == 0:
            player.take_hit(monster.get_hit_points(), monster.get_name())
            # Displays the player's status after the attack
            player.get_status()


# Pick a different monster based on the player's level
def pick_monster(level, player):
    if level == 1:
        monster_obj = Fluffy(player.get_health(), player.get_hit_points())
    elif level == 2:
        monster_obj = Ghost(player.get_health(), player.get_hit_points())
    elif level == 3:
        monster_obj = Clown(player.get_health(), player.get_hit_points())
    else:
        monster_obj = Monster()

    return monster_obj


# Check health of player, levels up player, and moves player to next level
def check_health(player, monster):
    if player.get_health() <= 0:
        print "You just died, retry!"
    elif monster.get_health() <= 0:
        print "You killed " + monster.get_name() + "!"

        # If player kills monster, then player's level raises by 1
        player.raise_level()

        # If there are still levels to play, then start the next level
        if player.get_level() <= 3:
            player_choice(player.get_level(), player)


# Engine of game
def player_choice(level, player):

    # Creates a monster based on the level of the player
    monster = pick_monster(level, player)

    # Displays user the Monster's information
    print "You are now facing monster " + monster.get_name()
    print "It has " + str(monster.get_health()) + " health and has " + str(monster.get_hit_points()) + " hit points."

    # Keeps player attacking if player and monster are still alive
    while player.get_health() > 0 and monster.get_health() > 0:
        choice = raw_input("Would you like to attack? ")

        if choice.lower() == "yes" or choice.lower() == "y":
            # Attacks the monster with player's hit points
            monster.take_hit(player.get_hit_points())
            # Displays monster's health status
            monster.get_status()

            # Monster's random attach
            random_monster_attack(player, monster)
        else:
            # If player does not attack, then monster attacks
            player.take_hit(monster.get_hit_points(), monster.get_name())
            # Displays player's health status
            player.get_status()

        # Checks user's and monster's health when player's or monster's health are 0 or less
        check_health(player, monster)


# Starts game and lets player pick a name - Only called once per game
def start_game():
    player_name = raw_input("Name of player: ")

    # Creates player
    player = Player(player_name)

    player.display_player_config()

    player_choice(1, player)


# Runs game
display_menu()