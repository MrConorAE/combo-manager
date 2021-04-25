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
combos = [
    Combo("Value", {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00}),
    Combo("Cheezy", {"Cheeseburger": 6.69,
          "Fries": 1.00, "Fizzy drink": 1.00}),
    Combo("Super", {"Cheeseburger": 6.69,
          "Large fries": 2.00, "Smoothie": 2.00})
]

# FUNCTIONS


def displayCombo(combo):
    """This function formats a combo into a human-readable string for display.

    Args:
        combo (Combo): The combo to display.

    Returns:
        String: The formatted string containing the combo details. Contains 2 leading newlines, for when displaying in a list.
    """
    output = ""
    output += f"\n\nName: {combo.name}\nItems:"
    for item in combo.items:
        # The ":.2f" ensures that the price is displayed properly.
        output += f"\n- {item} - ${combo.items[item]:.2f}"
    return output


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


def viewAllCombos(combos):
    """This function displays all the saved combos in a message box.

    Args:
        combos (List[Combo])): A list containing Combo objects of which to display.
    """
    output = ""
    if (len(combos) == 0):
        # If length of list is 0, print a placeholder message
        output = "There are no combos to display."
    else:
        # Otherwise, iterate over all combos, generating a string for each
        for combo in combos:
            output += displayCombo(combo)
    # Display output
    easygui.msgbox(output, "All Combos - Combo Manager", "Back to Menu")


def chooseCombo(combos, message):
    """This function will display a list of combo names and allows the user to select one for use.

    Args:
        combos (List[Combo]): A list of combos to choose from.
        message (String): A message to display in the selection window.

    Returns:
        Integer: The index of the item chosen in the combos list.
    """
    names = []
    for combo in combos:
        # Get a list of the names
        names.append(combo.name)
    # Once a selection has been made, return the ID
    selection = easygui.choicebox(
        message, "Choose a Combo - Combo Manager", names)
    if selection == None:
        # They pressed Cancel
        return None
    else:
        # They chose one
        return names.index(selection)


def editCombo(combos, pos):
    """This function allows the user to edit an existing combo.

    Args:
        combos (List[Combo]): The list of combos.
        pos (Index): The index of the combo to edit in the list 'combos'.
    """
    # Get the combo to edit, and make a new blank one to store the results in
    oldcombo = combos[pos]
    newcombo = Combo(None, {})
    # fields & values are lists of the keys & values for every attribute of the combo
    # in format (combo name, item name, item price, item name, item price, ...)
    # It's used for defining the titles & initial values in a multenterbox for editing
    values = [oldcombo.name]
    fields = ["Combo Name:"]
    for index, item in enumerate(oldcombo.items):
        values.append(item)
        fields.append(f"Item {index+1} Name:")
        values.append(oldcombo.items[item])
        fields.append(f"Item {index+1} Price: $")
    # Now display the editing box:
    while True:
        result = easygui.multenterbox(
            f"Editing combo '{oldcombo.name}'.\nEnter the new data and press OK to save. Press Cancel to add another item.\n(You will be able to review the edited combo before saving it.)", "Edit Combo - Combo Manager", fields, values)
        if (result == None):
            # Cancel pressed - add another set of fields.
            values.append("")
            fields.append(f"Item {len(fields)+1} Name:")
            values.append(0)
            fields.append(f"Item {len(fields)+1} Price: $")
        else:
            # We have changes!
            # First, get the name.
            newcombo.name = result[0]
            result.pop(0)
            # Now, iterate over every second item returned and save it.
            # It's every SECOND because the values are name/value pairs.
            for index in range(0, len(result), 2):
                newcombo.items[result[index]] = float(result[index+1])
            # Now allow the user to compare and decide to commit the changes.
            if (easygui.ynbox(f"Commit the changes to this combo? \n\n BEFORE =========={displayCombo(oldcombo)} \n\n AFTER =========={displayCombo(newcombo)}")):
                # Save changes!
                # First, remove the old combo.
                combos.pop(pos)
                # Now, reinsert the new one where the old one was.
                combos.insert(pos, newcombo)
                # Notify the user.
                easygui.msgbox(
                    f"Your changes to combo '{oldcombo.name}' were saved successfully.", "Edit Combo - Combo Manager", "Back to Menu")
                break
            else:
                # If they don't like the changes, ask for what to do next:
                if (easygui.buttonbox("Would you like to modify your changes, or abort editing altogether?", "Edit Combo - Combo Manager", ["Modify my changes", "Abort editing and discard changes"]) == "Abort editing and discard changes"):
                    # Abort editing: drop changes and go back to menu.
                    easygui.msgbox(
                        f"Editing cancelled. Your changes to combo '{oldcombo.name}' were not saved.", "Edit Combo - Combo Manager", "Back to Menu")
                    break
                else:
                    # Back to editing!
                    pass


def deleteCombo(combos, pos):
    if (easygui.ynbox(f"Are you sure you want to delete the combo '{combos[pos].name}'?\nThe combo will be permanently deleted. This cannot be undone.", "Delete Combo - Combo Manager", ["No, do not delete", "Yes, delete"]) == 0):
        combos.pop(pos)
        easygui.msgbox("The combo was deleted successfully.",
                       "Delete Combo - Combo Manager", "Back to Menu")
    else:
        easygui.msgbox("The combo was not deleted.",
                       "Delete Combo - Combo Manager", "Back to Menu")


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
        viewAllCombos(combos)
    elif (option == options[2]):
        # Edit a combo.
        choice = chooseCombo(combos, "Please select a combo to edit:")
        if (choice == None):
            # They pressed Cancel.
            pass
        else:
            editCombo(combos, choice)
    elif (option == options[3]):
        # Delete a combo.
        choice = chooseCombo(combos, "Please select a combo to delete:")
        if (choice == None):
            # They pressed Cancel.
            pass
        else:
            deleteCombo(combos, choice)
    elif (option == options[4]):
        # Quit.
        if (easygui.ynbox("Are you sure you want to quit Combo Manager?", "Quit - Combo Manager", ["No, do not quit", "Yes, quit"]) == 0):
            # Yes, quit.
            exit()
        else:
            # No, do not quit.
            pass
