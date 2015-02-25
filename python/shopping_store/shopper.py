from os import system

from cart import Cart


class Shopper(object):

    shopping_cart = Cart()

    def __init__(self):
        self.shopper_name = None
        self.shopper_email = None
        self.shopper_password = None
        self.shopper_cash = None

    def create_user(self, name, email, password, cash):
        self.shopper_name = name
        self.shopper_email = email
        self.shopper_password = password
        self.shopper_cash = cash

    def get_username(self):
        return self.shopper_email

    def buy_item(self, shopping_cart):

        cart_total = 0.00

        for i in shopping_cart:
            cart_total += float(i[1]) * float(i[2])

            # Remove all items from cart
            self.shopping_cart.set_shopping_cart([])

        self.shopper_cash -= cart_total

    def display_user_account_info(self):
        system('clear')
        print "Your Information"
        print "Your Name: " + self.shopper_name
        print "Your Cash: $" + str(self.shopper_cash)

        print "Shopping cart items: "

        if len(self.shopping_cart.shopping_cart) == 0:
            print "No items in shopping cart"
        else:
            print "=" * 20
            for i in self.shopping_cart.shopping_cart:
                print i[0] + "   $" + str(i[1]) + "   " + str(i[2]) + " units"
            print "=" * 20