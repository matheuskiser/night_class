# Show all cards in the deck
def show_all_cards_in_deck(deck_dict):
    for card in deck_dict:
            print card[0] + " of " + card[1]


# Returns cards that contain the suit the user picked
def pull_suit_cards(deck_dict):
    suit_chosen = raw_input("What card suit would you like to display? ")
    for card in deck_dict:
        for suit in card:
            if suit == suit_chosen.lower():
                print card[0] + " of " + card[1]


# Returns cards that contain the color the user picked
def pull_color_cards(deck_dict):
    color_chosen = raw_input("What card color would you like to display? ")
    for card in deck_dict:
        for color in card:
            if color == color_chosen.lower():
                print card[0] + " of " + card[1]


# Display menu to user
def display_menu():
    option = 0

    while option != 4:
        print "1. Show all cards"
        print "2. Show certain color"
        print "3. Show certain suit"
        print "4. Exit"
        option = int(raw_input("Pick a menu option: "))
        pick_option(option)


# Pick menu option
def pick_option(option):
    if option == 1:
        # Show all cards in the deck
        show_all_cards_in_deck(deck)
    elif option == 2:
        # Show only a certain color of cards
        pull_color_cards(deck)
    elif option == 3:
        # Show only a certain suit of cards
        pull_suit_cards(deck)
    elif option == 4:
        # Exit program
        print "Thanks for using our program!\n"


# Setup card lists
card_values = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
card_colors_blacks = ["black"]
card_colors_reds = ["red"]
card_suits_blacks = ["clubs", "spades"]
card_suits_reds = ["diamonds", "hearts"]
deck = []

# Combines black cards with their suits and values
for i in card_suits_blacks:
    for j in card_values:
        for k in card_colors_blacks:
            deck.append([j, i, k])

# Combines red cards with their suits and values
for r in card_suits_reds:
    for t in card_values:
        for y in card_colors_reds:
            deck.append([t, r, y])

# Start program
display_menu()