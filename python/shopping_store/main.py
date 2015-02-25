from shopper import Shopper
from login import Login
from store import Store

import os
import sqlite3

# TODO: Load items from catalog to program
# TODO: Authenticate user
# TODO: Save items and quantities to database

# Creates instance of database
db = sqlite3.connect('store_db')
cursor = db.cursor()

# Starts store and sets up all items
store = Store("Fred Meyer", "Portland, OR", 100)
store.store_setup()

# Starts user
user = Shopper()


# Starts database
def start_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, first_name TEXT, cash TEXT)
    ''')
    db.commit()


# Gets arguments to store a new entry to database
def save_entry_db(username, password, name, cash):
    # Insert entry
    cursor.execute('''INSERT INTO users(username, password, first_name, cash) VALUES(?,?,?,?)''', (username, password, name, cash))
    db.commit()


# Reads the database, gets logged in user
def login_create_user(user_name, password):
    # Tries to login with given credentials. If username does not exist, throw error
    try:
        cursor.execute("SELECT * FROM users WHERE username=?", [user_name])
        user_db = cursor.fetchone()

        # Checks user's password with what is in db
        if password == user_db[2]:
            user.create_user(user_db[3], user_db[1], user_db[2], user_db[4])
        else:
            clear()
            print "Incorrect login. Try again!"
            user_login()
    except TypeError:
        clear()
        print "Incorrect login. Try again!"
        user_login()


def clear():
    os.system('clear')


def intro():
    clear()
    print "Welcome to Fred Meyer!"
    has_account = raw_input("Do you already have an account? (y/n) ")
    if has_account.lower() == "y" or has_account.lower() == "yes":
        user_login()
    else:
        user_register()


def user_register():
    print "To register, enter the following information"
    name = raw_input("Name: ")
    email = raw_input("Email: ")
    password = raw_input("Password: ")
    cash = float(raw_input("How much money do you have? "))

    # Create user in class
    user.create_user(name, email, password, cash)
    # Creates user in db
    save_entry_db(email, password, name, cash)

    clear()
    user_login()


def user_login():
    print "To login, enter you credentials below"
    email = raw_input("Email: ")
    password = raw_input("Password: ")

    # Create shopper from database
    login_create_user(email, password)

    # Logs in user with the store
    Login(email, password)


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


def show_items():
    clear()
    store.display_all_items()


def search_item():
    clear()
    item_name = raw_input("Search item: ")
    store.display_single_item(item_name)
    choice = raw_input("Buy item? (y/n): ")

    if choice.lower() == "y" or choice.lower() == "yes":
        user_qty = int(raw_input("How many? "))
        item_qty = store.get_item_qty(item_name)

        if item_qty != 0:
            # If user is trying to buy more qty than store has
            while user_qty > item_qty:
                print "Sorry, quantity entered is too high. Try again"
                user_qty = int(raw_input("How many? "))

            user.add_to_cart(item_name, store.get_single_item_cost(item_name), user_qty)
            store.remove_qty_from_item(item_name, user_qty)
            print "Item added to cart."
        else:
            print "Item not in stock."


def display_user_account():
    user.display_user_account_info()


def checkout():
    clear()
    cart_list = user.return_cart_list()

    print "Here is your shopping cart..."
    if len(cart_list) == 0:
        print "No items in shopping cart"
    else:
        print "=========================================================="
        for i in cart_list:
            print i[0] + "   $" + str(i[1]) + "   " + str(i[2]) + " units"
        print "=========================================================="
        print "Total: $" + str(user.display_shopping_cart_total())

    wants_checkout = raw_input("Are you sure you want to checkout? ")
    if wants_checkout.lower() == "y" or wants_checkout.lower() == "yes":

        # Checkout user
        user.buy_item(cart_list)
        # Checkout store
        store.buy_item(cart_list)

        print "Thanks for shopping!"
        exit(0)


start_db()

intro()

user_menu()