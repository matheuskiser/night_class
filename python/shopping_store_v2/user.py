import sqlite3

from cart import Cart


class User(Cart):
    def __init__(self):
        super(User, self).__init__()
        self.username = ""
        self.name = ""
        self.password = ""
        self.cash = ""

        # Creates instance of database
        self.db = sqlite3.connect('store_db')
        self.cursor = self.db.cursor()

        # Starts user db
        self.start_db()

    def create_app_user(self, username, password):
        self.username = username
        self.password = password
        self.name = self.get_user_name(username)
        self.cash = self.get_user_cash(username)

    def start_db(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT,"
                            " password TEXT, first_name TEXT, cash TEXT)")
        self.db.commit()

    def get_user_name(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", [username])
        user_db = self.cursor.fetchone()
        return user_db[3]

    def get_user_cash(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", [username])
        user_db = self.cursor.fetchone()
        return user_db[4]

    def get_user_id(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", [username])
        user_db = self.cursor.fetchone()
        return user_db[0]

    def display_user_account_info(self):
        print "Your Information"
        print "Your Name: " + self.name
        print "Your Cash: $" + str(self.cash)
        print "Your Shopping Cart:"
        self.print_shopping_cart(self.username)

    def checkout_cart(self, user_id):
        # Display user's cart
        self.print_shopping_cart(self.username)
        wants_checkout = raw_input("\nAre you sure you want to checkout? ")
        if wants_checkout.lower() == "y" or wants_checkout.lower() == "yes":
            # Gets cart total, removes cash, and empties cart
            cart_total = self.get_cart_total_amount(user_id)
            user_cash = float(self.cash) - float(cart_total)

            # Updates user's cash
            self.cursor.execute("UPDATE users SET cash =? WHERE ID =?;", [user_cash, user_id])
            self.db.commit()

            # Empties cart
            self.remove_cart(user_id)

            print "Thanks for shopping!"
            exit(0)
