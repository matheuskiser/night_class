from items import Items


class Store(object):
    def __init__(self, name, location, cash):
        self.store_name = name
        self.store_location = location
        self.store_cash = cash
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_all_items(self):
        for i in self.items:
            print i.item_name, i.item_cost, i.item_qty

    def store_setup(self):
        banana = Items("Banana", 1.85, 10)
        apple = Items("Apple", 2.95, 20)
        cookie = Items("Cookie", 0.95, 15)

        self.add_item(banana)
        self.add_item(apple)
        self.add_item(cookie)

    def buy_item(self, name, qty):
        for i in self.items:
            if i.item_name == name:
                i.item_qty -= int(qty)
                total_sale = i.item_qty * i.item_cost
                self.store_cash += total_sale