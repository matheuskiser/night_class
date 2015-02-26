import sqlite3


class Store(object):
    def __init__(self, name, location):
        self.store_name = name
        self.store_location = location

        # Creates instance of database
        self.db = sqlite3.connect('store_db')
        self.cursor = self.db.cursor()

        # Starts items db
        self.start_items_db()

    def load_items_store(self):
        # Loads items to store item's list
        self.cursor.execute("INSERT INTO items(item_name, item_qty, item_cost) "
                            "VALUES(?,?,?)", ("Banana", "20", "3.99"))
        self.cursor.execute("INSERT INTO items(item_name, item_qty, item_cost) "
                            "VALUES(?,?,?)", ("Apple", "20", "4.99"))
        self.cursor.execute("INSERT INTO items(item_name, item_qty, item_cost) "
                            "VALUES(?,?,?)", ("Cookie", "20", "5.99"))
        self.db.commit()

    def print_all_items(self):
        self.cursor.execute("SELECT * FROM items")
        store_items = self.cursor.fetchall()

        for i in store_items:
            print "Name: " + i[1] + ", Qty: " + i[2] + ", $" + i[3]

    def print_single_item(self, item_name):
        self.cursor.execute("SELECT * FROM items WHERE item_name=?", [item_name])
        single_item = self.cursor.fetchone()

        print "Name: " + single_item[1] + ", Qty: " + single_item[2] + ", $" + single_item[3]

    def get_item_qty(self, item_name):
        self.cursor.execute("SELECT item_qty FROM items WHERE item_name=?", [item_name])
        item_qty = self.cursor.fetchone()

        return item_qty[0]

    def get_item_cost(self, item_name):
        self.cursor.execute("SELECT item_cost FROM items WHERE item_name=?", [item_name])
        item_cost = self.cursor.fetchone()

        return item_cost[0]

    def remove_item_qty(self, item_name, qty):
        self.cursor.execute("UPDATE items SET item_qty =? WHERE item_name =?;", [qty, item_name])
        self.db.commit()

    def start_items_db(self):
        # Creates db for items
        self.cursor.execute("CREATE TABLE IF NOT EXISTS items(ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                            " item_name TEXT, item_qty TEXT, item_cost TEXT)")
        self.db.commit()


if __name__ == '__main__':
    store = Store('a', 'b')