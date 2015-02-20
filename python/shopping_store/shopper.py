class Shopper(object):
    def __init__(self):
        self.shopper_name = None
        self.shopper_email = None
        self.shopper_password = None
        self.shopper_cash = None
        self.shopper_cart = []

    def create_user(self, name, email, password, cash):
        self.shopper_name = name
        self.shopper_email = email
        self.shopper_password = password
        self.shopper_cash = cash