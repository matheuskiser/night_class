import sqlite3

from items import Items


class Cart():

    def __init__(self):
        self.shopping_cart = []

        # Creates instance of database
        self.db = sqlite3.connect('store_db')
        self.cursor = self.db.cursor()

        # Starts user db
        self.start_cart_db()

    def set_shopping_cart(self, cart):
        self.shopping_cart = cart

    def add_to_cart(self, user_id, name, qty, cost):
        item = [name, qty, cost]
        self.shopping_cart.append(item)

        # Add cart to db
        self.save_shopping_cart(user_id, name, qty, cost)

    def return_cart_list(self, user_name):
        # Gets data from cart db to get user ID
        self.cursor.execute("SELECT ID FROM users WHERE username=?", [user_name])
        user_id = self.cursor.fetchone()

        # Gets cart from carts table matching user ID
        self.cursor.execute("SELECT * FROM carts WHERE user_id=?", [user_id[0]])
        user_cart = self.cursor.fetchone()

        return user_cart

    def display_shopping_cart_total(self):
        total_amount = 0.00

        print self.shopping_cart

        # for i, value in self.shopping_cart:
        #     # total_amount += float(value[1]) * float(value[2])

        # return total_amount

    def create_shopping_cart(self, user_name):
        # Gets data from cart db to get user ID
        self.cursor.execute("SELECT ID FROM users WHERE username=?", [user_name])
        user_id = self.cursor.fetchone()

        # Gets cart from carts table matching user ID
        self.cursor.execute("SELECT * FROM carts WHERE user_id=?", [user_id[0]])
        user_cart = self.cursor.fetchone()

        # Adds cart to user
        self.add_to_cart(user_cart[1], user_cart[2], user_cart[3])

    def save_shopping_cart(self, user_id, name, qty, cost):
        # Saves cart to user's account
        self.cursor.execute("INSERT INTO carts(user_id, item_name, item_qty, item_cost) "
                            "VALUES(?,?,?,?)", (user_id, name, qty, cost))
        self.db.commit()

    def start_cart_db(self):
        # Creates db for shopping cart
        self.cursor.execute("CREATE TABLE IF NOT EXISTS carts(ID INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT,"
                            " item_name TEXT, item_qty TEXT, item_cost TEXT)")
        self.db.commit()