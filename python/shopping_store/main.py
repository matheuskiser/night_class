from shopper import Shopper
from store import Store
from login import Login
from items import Items
from departments import ClothingDepartment

import os

# Starts store
store = Store("Fred Meyer", "Portland, OR", 100)


def intro():
    os.system('clear')
    print "Welcome to Fred Meyer!"
    user_login()


def user_login():
    print "To login, enter you credentials below"
    name = raw_input("Name: ")
    cash = raw_input("How much money do you have? ")
    email = raw_input("Email: ")
    password = raw_input("Password")

    # Logs in user with the store
    Login(email, password)

    # Get user
    user = Shopper(name, email, password, cash)


def make_items():
    clothing = ClothingDepartment()
    item = Items("Polo Shirt", 10, 20, "Clothing")
    clothing.add_item(item)


