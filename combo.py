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

# FUNCTIONS


def addCombo():
    """
    This function creates a new combo to add to the combos list, and asks for confirmation.
    """
    while True:
        # Error checking loop
        try:
            name = easygui.multenterbox(
                "Please enter the name for your new combo, or press Cancel to abort:", "New Combo (1/3) - Combo Manager", ["Name:"])[0]
            if name == "":
                # If result is empty:
                easygui.msgbox(
                    "Error: combos must have names.", "New Combo - Combo Manager", "Try again")
            else:
                # If OK, break loop and continue
                break
        except:
            # If any other error:
            easygui.msgbox(
                "Error: combos must have names.", "New Combo - Combo Manager", "Try again")
    items = {}
    while True:
        # Loop while more items to add
        nextitem = ["", 0]
        while True:
            # Error checking loop
            nextitem = easygui.multenterbox(
                f"Please enter item {len(items)+1} in the combo '{name}' and press OK, or press Cancel if you have entered all the items already:\n(You will be able to review the combo before adding.)", "New Combo (2/3) - Combo Manager", ["Item Name:", "Item Price: $"], [(nextitem[0] if nextitem != None else ""), (nextitem[1] if nextitem != None else "")])
            try:
                if (nextitem == None):
                    # If cancelled, break (no more items)
                    break
                else:
                    # If OK, store & continue to next item
                    items[nextitem[0]] = float(nextitem[1])
                    break
            except:
                # If error (normally NaN), alert & try again
                easygui.msgbox("Error: prices must be numbers.",
                               "New Combo - Combo Manager")
        if (nextitem == None):
            # If cancelled, break (no more items)
            break
    formatteditems = ""
    for item in items:
        # Generate a displayable version of the combo about to be added
        formatteditems += f"- {item} (${items[item]})\n"
    # Generate the combo
    newcombo = Combo(name, items)
    # Ask for confirmation
    if (easygui.ynbox(f"Add this combo?\n\nName: {name}\nItems:{formatteditems}")):
        # Yes, add
        combos.append(newcombo)
        easygui.msgbox(f"The combo '{name} was added.",
                       "New Combo - Combo Manager", "Back to Menu")
    else:
        # No, do not add
        easygui.msgbox(f"The combo '{name}' was not added.",
                       "New Combo - Combo Manager", "Back to Menu")


# MAIN MENU
while True:
    # List of options:
    options = ["Add Combo", "View All", "Edit Combo", "Delete Combo", "Quit"]
    option = easygui.buttonbox(
        "Welcome to Combo Manager!\n\nWhat would you like to do?", "Main Menu - Combo Manager", options)
    if (option == options[0]):
        # Add a combo to the list.
        addCombo()
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
