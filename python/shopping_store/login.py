import sqlite3
import os


class Login(object):
    def __init__(self):
        self.cred_email = ""
        self.cred_password = ""

        # Creates instance of database
        self.db = sqlite3.connect('store_db')
        self.cursor = self.db.cursor()

        # Starts user db
        self.start_db()

    @staticmethod
    def clear():
        os.system('clear')

    def login_factory(self, email, password):
        self.cred_email = email
        self.cred_password = password

    # Returns user's db ID
    def get_id(self, user_name):
        self.cursor.execute("SELECT ID FROM users WHERE username=?", [user_name])
        user_id = self.cursor.fetchone()
        return user_id[0]

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
    def login_create_user(self, user_name, password, shopper_obj):
        # Tries to login with given credentials. If username does not exist, throw error
        try:
            self.cursor.execute("SELECT * FROM users WHERE username=?", [user_name])
            user_db = self.cursor.fetchone()

            # Checks user's password with what is in db
            if password == user_db[2]:
                # shopper = Shopper()
                shopper_obj.create_user(user_db[3], user_db[1], user_db[2], float(user_db[4]))
            else:
                self.clear()
                print "Incorrect login. Try again!"
                self.user_login(shopper_obj)
        except TypeError:
            self.clear()
            print "Incorrect login. Try again!"
            self.user_login(shopper_obj)

    def user_login(self, shopper_obj):
        print "To login, enter you credentials below"
        email = raw_input("Email: ")
        password = raw_input("Password: ")

        # Create shopper from database
        self.login_create_user(email, password, shopper_obj)

        # Logs in user with the store
        self.login_factory(email, password)