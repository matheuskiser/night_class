class Shopper(object):
    def __init__(self, name, email, password, cash):
        self.shopper_name = name
        self.shopper_email = email
        self.shopper_password = password
        self.shopper_cash = cash
        self.shopper_cart = []