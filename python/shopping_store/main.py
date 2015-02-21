from shopper import Shopper
from login import Login
from store import Store

import os

# Starts store and sets up all items
store = Store("Fred Meyer", "Portland, OR", 100)
store.store_setup()

# Starts user
user = Shopper()


def clear():
    os.system('clear')


def intro():
    clear()
    print "Welcome to Fred Meyer!"
    user_login()


def user_login():
    print "To login, enter you credentials below"
    name = raw_input("Name: ")
    email = raw_input("Email: ")
    password = raw_input("Password: ")
    cash = int(raw_input("How much money do you have? "))

    # Logs in user with the store
    Login(email, password)

    # Get user
    user.create_user(name, email, password, cash)


def user_menu():
    clear()

    option = 0

    while option != 5:
        print "==================================="
        print "Menu"
        print "==================================="
        print "1. Browse all items"
        print "2. Buy item"
        print "3. View carts"
        print "4. Checkout"
        print "5. Exit"
        option = int(raw_input("Pick an option: "))
        user_pick_menu_option(option)


def user_pick_menu_option(option):
    if option == 1:
        """Show Items"""
        show_items()
    elif option == 2:
        """Buy Item"""
        buy_item()
    elif option == 3:
        """View Carts"""
    elif option == 4:
        """Checkout"""
    elif option == 5:
        """Exit Program"""
        clear()
        print "Thanks for shopping!"


def show_items():
    clear()
    store.get_all_items()


def buy_item():
    clear()

    item_name = raw_input("What item do you want to buy? ")
    item_qty = raw_input("How many? ")

    store.buy_item(item_name, item_qty)
    # user.buy_item()


intro()

user_menu()