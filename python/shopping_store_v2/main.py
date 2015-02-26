from store import Store
from login import Login

import os


# Starts store and sets up all items
store = Store("Fred Meyer", "Portland, OR")

# Temporary code to load or not load items
load = raw_input("Load items? ")
if load == "y":
    store.load_items_store()

# Starts user's login
user = Login()

# Global user ID
USER_ID = user.user.get_user_id(user.user.username)


def clear():
    os.system('clear')


def user_menu():
    clear()
    option = 0
    while option != 5:
        print "==================================="
        print "Menu"
        print "==================================="
        print "1. Browse all items"
        print "2. Search"
        print "3. User account"
        print "4. Checkout"
        print "5. Exit"
        option = int(raw_input("Pick an option: "))
        user_pick_menu_option(option)


def user_pick_menu_option(option):
    if option == 1:
        """Show Items"""
        show_items()
    elif option == 2:
        """Search item"""
        search_item()
    elif option == 3:
        """Show account info"""
        display_user_account()
    elif option == 4:
        """Checkout"""
        checkout()
    elif option == 5:
        """Exit Program"""
        clear()
        print "Thanks for shopping!"


# Outputs all items from store
def show_items():
    clear()
    store.print_all_items()


# Searches item in store and asks user to buy item
def search_item():
    clear()
    print "Search item:"
    item_name = raw_input("What is the item's name? ")

    # Shows item searched
    store.print_single_item(item_name)

    # Asks user to buy item
    choice = raw_input("Buy item? (y/n): ")
    if choice.lower() == "y" or choice.lower() == "yes":
        user_qty = raw_input("How many? ")
        item_qty = store.get_item_qty(item_name)
        item_cost = store.get_item_cost(item_name)

        if int(item_qty) > 0:
            # If user is trying to buy more qty than store has
            while int(user_qty) > int(item_qty):
                print "Sorry, quantity entered is too high. Try again"
                user_qty = int(raw_input("How many? "))

            # Gets item amount after adding to cart
            qty_left = int(item_qty) - int(user_qty)
            # Adds item to cart
            user.user.add_to_cart(USER_ID, item_name, user_qty, item_cost)
            # Remove item qty from item in store
            store.remove_item_qty(item_name, qty_left)
            print "Item added to cart."
        else:
            print "Item not in stock."


def display_user_account():
    clear()
    user.user.display_user_account_info()


def checkout():
    clear()
    user.user.checkout_cart(USER_ID)


# RUNS PROGRAM

# Checks if user is logged in
if user.is_logged_in:
    user_menu()