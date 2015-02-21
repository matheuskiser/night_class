from os import system


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

    def buy_item(self, shopping_cart):

        cart_total = 0.00

        for i in shopping_cart:
            cart_total += float(i[1]) * float(i[2])

            # Remove all items from cart
            self.shopper_cart = []

        self.shopper_cash -= cart_total

    def add_to_cart(self, name, qty, cost):
        item = [name, qty, cost]
        self.shopper_cart.append(item)

    def return_cart_list(self):
        return self.shopper_cart

    def display_shopping_cart_total(self):
        total_amount = 0.00

        for i in self.shopper_cart:
            total_amount += float(i[1]) * float(i[2])

        return total_amount

    def display_user_account_info(self):
        system('clear')
        print "Your Information"
        print "Your Name: " + self.shopper_name
        print "Your Cash: $" + str(self.shopper_cash)

        print "Shopping cart items: "

        if len(self.shopper_cart) == 0:
            print "No items in shopping cart"
        else:
            print "=" * 20
            for i in self.shopper_cart:
                print i[0] + "   $" + str(i[1]) + "   " + str(i[2]) + " units"
            print "=" * 20