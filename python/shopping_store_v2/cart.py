import sqlite3


class Cart(object):
    def __init__(self):
        # Creates instance of database
        self.db = sqlite3.connect('store_db')
        self.cursor = self.db.cursor()

        # Starts user db
        self.start_cart_db()

    def start_cart_db(self):
        # Creates db for shopping cart
        self.cursor.execute("CREATE TABLE IF NOT EXISTS carts(ID INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT,"
                            " item_name TEXT, item_qty TEXT, item_cost TEXT)")
        self.db.commit()

    def add_to_cart(self, user_id, name, qty, cost):
        # Saves cart to user's account
        self.cursor.execute("INSERT INTO carts(user_id, item_name, item_qty, item_cost) "
                            "VALUES(?,?,?,?)", (user_id, name, qty, cost))
        self.db.commit()

    def print_shopping_cart(self, username):
        # Gets data from cart db to get user ID
        self.cursor.execute("SELECT ID FROM users WHERE username=?", [username])
        user_id = self.cursor.fetchone()

        # Gets cart from carts table matching user ID
        self.cursor.execute("SELECT * FROM carts WHERE user_id=?", [user_id[0]])
        user_cart = self.cursor.fetchall()

        total_amount = 0.00

        for i in user_cart:
            print "Name: " + i[2] + ", Qty: " + i[3] + ", $" + i[4]
            total_amount += float(i[3]) * float(i[4])

        print "Total: $" + str(total_amount)

    def get_cart_total_amount(self, user_id):
        # Gets cart from carts table matching user ID
        self.cursor.execute("SELECT * FROM carts WHERE user_id=?", [user_id])
        user_cart = self.cursor.fetchall()

        total_amount = 0.00

        for i in user_cart:
            total_amount += float(i[3]) * float(i[4])

        return total_amount

    def remove_cart(self, user_id):
        self.cursor.execute("DELETE FROM carts WHERE user_id =?;", [user_id])
        self.db.commit()



if __name__ == '__main__':
    Cart()
