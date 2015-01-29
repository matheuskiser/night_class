# Declare dictionary variable
phone_book_dictionary = {'Matheus': {'fname': 'Matheus', 'lname': 'Iser', 'phone_number': '503-333-4657'}}

# Functions
def change_entry():
    print "\n"
    change_value = raw_input("Enter first name to change something in the entry: ")

    search(change_value)

    remove_entry(change_value)

    print "\nEdit this entry"
    add_value()


def search(search_term):
    for key, value in phone_book_dictionary.items():
        if key == search_term:
            print "First Name: " + value['fname']
            print "Last Name: " + value['lname']
            print "Phone Number: " + value['phone_number']
            print "\n"


def remove_entry(removed_entry):
    for key, value in phone_book_dictionary.items():
        if key == removed_entry:
            phone_book_dictionary.pop(key)


def print_phone_book():
    print "\n"
    for key in phone_book_dictionary.values():
        print "First Name: " + key['fname']
        print "Last Name: " + key['lname']
        print "Phone Number: " + key['phone_number']
        print "\n"


def add_value():
    add_entry_fname = raw_input("First name: ")
    add_entry_lname = raw_input("Last name: ")
    add_entry_phone_number = raw_input("Phone number: ")

    phone_book_dictionary[add_entry_fname] = {'fname': add_entry_fname, 'lname': add_entry_lname, 'phone_number': add_entry_phone_number}

    print "\n"


def display_menu():
    option = "0"
    while option != "6":
        print "Welcome to the Phone Book Program!"
        print "1. Show entries"
        print "2. Add an entry"
        print "3. Remove an entry"
        print "4. Search"
        print "5. Change an entry"
        print "6. Quit"
        option = raw_input("Pick an item: ")
        pick_option(option)


def pick_option(option):
    if option == "1":
        #Show entries
        print_phone_book()
    elif option == "2":
        #add entry
        print "\n"
        print "Add an entry: "
        add_value()
    elif option == "3":
        #remove entry
        print "\n"
        removed_entry = raw_input("Enter entry you want to remove: ")
        remove_entry(removed_entry)
        print "Entry '" + removed_entry + "' has been removed.\n"
    elif option == "4":
        #search
        print "\n"
        search_term = raw_input("Enter a search term: ")
        search(search_term)
    elif option == "6":
        #quit
        print "Thanks for using our Phone Book."
    elif option == "5":
        #change entry
        change_entry()


display_menu()


