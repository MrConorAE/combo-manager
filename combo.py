# Combo Manager
# Copyright (c) Conor Eager, 2021. All rights reserved.

# IMPORTS
# Import EasyGUI for the graphical interface.
import easygui
# Import Pickle for saving and loading combos.
import pickle

# DATA STORAGE
# Defining the global variables and data structures used.


class Combo:
    """This class defines a combo of items.

    Args:
        name (str): The name of the combo.
        items (dict): A dictionary containing the names and prices (as float) of individual items in the combo.
    """

    def __init__(self, name, items):
        self.name = name
        self.items = items


# This array contains all the combos as Combo objects (defined above).
combos = []

# MAIN MENU
while True:
    # List of options:
    options = ["Add Combo", "View All", "Edit Combo", "Delete Combo", "Quit"]
    option = easygui.buttonbox(
        "Welcome to Combo Manager!\n\nWhat would you like to do?", "Main Menu - Combo Manager", options)
    if (option == options[0]):
        # Add a combo to the list.
        pass
    elif (option == options[1]):
        # View all combos.
        pass
    elif (option == options[2]):
        # Edit a combo.
        pass
    elif (option == options[3]):
        # Delete a combo.
        pass
    elif (option == options[4]):
        # Quit.
        if (easygui.ynbox("Are you sure you want to quit Combo Manager?", "Quit - Combo Manager", ["No, do not quit", "Yes, quit"]) == 0):
            # Yes, quit.
            exit()
        else:
            # No, do not quit.
            pass
