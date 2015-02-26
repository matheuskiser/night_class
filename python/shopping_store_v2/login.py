import sqlite3
import os

from user import User


class Login(object):

    user = User()
    is_logged_in = False

    def __init__(self):

        # Creates instance of database
        self.db = sqlite3.connect('store_db')
        self.cursor = self.db.cursor()

        # Starts user db
        self.start_db()

        self.intro()

    @staticmethod
    def clear():
        os.system('clear')

    # Starts user's database
    def start_db(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT,"
                            " password TEXT, first_name TEXT, cash TEXT)")
        self.db.commit()

    # Gets arguments to store a new entry to database
    def save_entry_db(self, username, password, name, cash):
        # Insert entry
        self.cursor.execute("INSERT INTO users(username, password, first_name, cash) "
                            "VALUES(?,?,?,?)", (username, password, name, cash))
        self.db.commit()

    # Reads the database, gets logged in user
    def login_user(self, user_name, password):
        # Tries to login with given credentials. If username does not exist, throw error
        try:
            self.cursor.execute("SELECT * FROM users WHERE username=?", [user_name])
            user_db = self.cursor.fetchone()

            # Checks user's password with what is in db
            if password == user_db[2]:
                # User matched
                self.is_logged_in = True
            else:
                print "Incorrect login. Try again!"
                self.login_dialog()
        except TypeError:
            print "Incorrect login. Try again!"
            self.login_dialog()

    def login_dialog(self):
        self.clear()
        print "To login, enter you credentials below"
        email = raw_input("Username: ")
        password = raw_input("Password: ")

        # Makes temp app user
        self.user.create_app_user(email, password)
        # Logs in user to app
        self.login_user(email, password)

    def user_register(self):
        self.clear()
        print "To register, enter the following information"
        name = raw_input("Name: ")
        email = raw_input("Username: ")
        password = raw_input("Password: ")
        cash = float(raw_input("How much money do you have? "))

        # Creates user in db
        self.save_entry_db(email, password, name, cash)
        # Go to login_dialog() after registration
        self.login_dialog()

    def intro(self):
        self.clear()
        print "Welcome to Fred Meyer!"
        has_account = raw_input("Do you already have an account? (y/n) ")
        if has_account.lower() == "y" or has_account.lower() == "yes":
            self.login_dialog()
        else:
            self.user_register()


if __name__ == '__main__':
    Login()