from items import Items


class Store(object):
    def __init__(self, name, location, cash):
        self.store_name = name
        self.store_location = location
        self.store_cash = cash
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_all_items(self):
        for i in self.items:
            print i.item_name, i.item_cost, i.item_qty

    def remove_qty_from_item(self, item_name, item_qty):
        for i in self.items:
            if i.item_name == item_name:
                i.item_qty -= item_qty

    def store_setup(self):
        banana = Items("Banana", 1.85, 10)
        apple = Items("Apple", 2.95, 20)
        cookie = Items("Cookie", 0.95, 15)

        self.add_item(banana)
        self.add_item(apple)
        self.add_item(cookie)

    def buy_item(self, shopping_cart):
        total_amount = 0.00

        for i in shopping_cart:
            self.remove_qty_from_item(i[0], i[1])
            total_amount += float(i[1]) * float(i[2])

        self.store_cash += total_amount

    def display_single_item(self, title):
        for i in self.items:
            if i.item_name == title:
                print "Name: " + i.item_name
                print "Cost: " + str(i.item_cost)
                print "Stock: " + str(i.item_qty)

    def get_single_item_cost(self, title):
        for i in self.items:
            if i.item_name == title:
                return i.item_cost

    def get_item_qty(self, title):
        for i in self.items:
            if i.item_name == title:
                return i.item_qty

    def return_item(self, title):
        for i in self.items:
            if i.item_name == title:
                return i