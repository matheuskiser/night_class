class Items(object):
    def __init__(self, name, cost, qty):
        self.item_name = name
        self.item_cost = cost
        self.item_qty = qty

    def get_item_name(self):
        return self.item_name

    def get_item_cost(self):
        return self.item_cost

    def get_item_qty(self):
        return self.item_qty