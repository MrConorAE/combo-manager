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

# The Help & About text
# This is what's displayed when you open Help on the main menu
help = {
    "Adding a combo to the menu": "To add a combo, click [Add Combo] on the main menu.\n\nIn the next box, type the name of the new combo to add, or press [Cancel] if you don't want to add a combo anymore.\n\nOnce you have entered a name, you'll be asked to enter the names and prices of each item in the combo. Type the name and price (don't include the dollar sign, that's added for you) for the item, then press [OK] to add it. Repeat until you have entered all the items, then press [Cancel] to finalise.\n\nAt this point, you'll be asked if you want to add the combo. Look over the combo displayed - this is what will be added - and press [Yes] if it's OK, or [No] if it isn't.\n\nIf you press [No], you'll be asked if you want to edit the combo and then be asked again ([Modify combo]) or just discard it entirely and go back to the main menu ([Abort creating and discard]).\n\nIf you press [Yes], the combo will be saved and you're done! Just press [Back to Menu] in the message box that appears to head back to the main menu.",
    "Viewing all the combos on the menu": "To view all the combos currently saved, click [View All] on the main menu.\nA new window will open, displaying all of the combos.\n\nTo print the entire menu, including formatting, to the Python Shell for easy copying or printing, click [Print to Shell].\n\nWhen you are done viewing the combos, press [Back to Menu] to return to the main menu.",
    "Editing a combo already on the menu": "To edit a combo, click [Edit Combo] on the main menu.\n\nA list of all the combos on the menu will be displayed - select the one you wish to edit and press [OK], or press [Cancel] if you don't want to edit anymore.\n\nWhen you have selected your combo, a window will open with the details of the combo filled in.\nIf you want to add more items, press [Cancel] to add 1 more item each time. Note that if you add a new item, any unsaved changes will be lost - so add all the blank items first, then fill them out to avoid retyping everything.\n\nTo delete an item, empty the field where the item name is displayed.\nIf you omit a name, the item will be skipped. If you omit a price, it will default to $0.\n\nWhen you are done editing, and you have made all the changes you want, press [OK].\nA new window will then appear, displaying the combo before your changes (under the heading 'BEFORE'), and after your changes ('AFTER'). If you want to keep the changes you have made, press [Yes] to save them. Otherwise, press [No].\n\nIf you press [No], you'll be asked if you want to edit the combo again ([Modify my changes]) or just discard your changes and go back to the main menu ([Abort editing and discard]).\n\nIf you press [Yes], the changes to the combo will be saved and you're done! Just press [Back to Menu] in the message box that appears to head back to the main menu.",
    "Deleting a combo": "To delete a combo from the menu, click [Delete Combo] on the main menu.\n\nA list of all the combos on the menu will be displayed - select the one you wish to remove and press [OK], or press [Cancel] to go back to the main menu.\n\nAfter you select a combo to delete, you'll be asked if you are sure you want to delete the combo.\n\nIf you are sure, and want to delete it permanently, click [Yes, delete].\nIf you do not want to delete the combo, click [No, do not delete].\n\nOnce you have made a choice, a message box will be displayed informing you of the choice you made and if it was successful. Just click [Back to Menu] to return to the main menu.",
    "Viewing help": "To view the help menu (like you are now), click [Help & About] on the main menu.\n\nA list of all the help topics available will be displayed. To view one, select it and click [OK]. To go back to the main menu, press [Cancel].\n\nOnce you have selected a topic, it will be displayed. To go back to the list of topics or the main menu, click [Back].",
    "About Combo Manager": "Combo Manager\n\nDeveloped by Conor Eager.\n\nCopyright (c) Conor Eager, 2021. All rights reserved."
}

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
    total = 0
    for item in combo.items:
        # The ":.2f" ensures that the price is displayed properly.
        output += f"\n- {item} - ${combo.items[item]:.2f}"
        total += combo.items[item]
    output += f"\nTotal: ${total:.2f}"
    return output


def addCombo():
    """
    This function creates a new combo to add to the combos list, and asks for confirmation.
    """
    while True:
        # Error checking loop
        try:
            name = easygui.multenterbox(
                "Please enter the name for your new combo, or press Cancel to abort:", "New Combo (Step 1/3) - Combo Manager", ["Name:"])
            if name == [""]:
                # If result is empty:
                easygui.msgbox(
                    "Error: combos must have names.", "New Combo - Combo Manager", "Try again")
            elif name == None:
                # Cancelled, exit.
                return
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
                f"Please enter item {len(items)+1} in the combo '{name}' and press OK, or press Cancel if you have entered all the items already:\n(You will be able to review the combo before adding.)", "New Combo (Step 2/3) - Combo Manager", ["Item Name:", "Item Price: $"], [(nextitem[0] if nextitem != None else ""), (nextitem[1] if nextitem != None else "")])
            try:
                if (nextitem == None):
                    # If cancelled, break (no more items)
                    break
                elif (nextitem[0] == ""):
                    # No item name.
                    easygui.msgbox("Skipping item with no name.",
                                   "New Combo - Combo Manager", "Continue")
                    break
                elif (nextitem[1] == "" or float(nextitem[1]) == 0):
                    # No item name.
                    easygui.msgbox("No price given, defaulting to 0.",
                                   "New Combo - Combo Manager", "Continue")
                    items[nextitem[0]] = 0
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
    while True:
        # "Save this combo?" loop
        # If they say No > Edit, this allows them to come back and edit multiple times
        # Generate the combo
        newcombo = Combo(name, items)
        # Ask for confirmation
        if (easygui.ynbox(f"Add this combo?{displayCombo(newcombo)}", "New Combo (Step 3/3) - Combo Manager")):
            # Yes, add
            combos.append(newcombo)
            easygui.msgbox(f"The combo '{name}' was added successfully.",
                           "New Combo - Combo Manager", "Back to Menu")
            return
        else:
            # No, do not add
            if (easygui.buttonbox("Would you like to modify the combo, or abort creating altogether?", "New Combo - Combo Manager", ["Modify combo", "Abort creating and discard"]) == "Abort creating and discard"):
                # Abort editing: drop changes and go back to menu.
                easygui.msgbox(
                    f"Creation cancelled. The combo '{newcombo.name}' was not added.", "New Combo - Combo Manager", "Back to Menu")
                return
            else:
                # Back to editing.
                # Instead of getting them to retype everything, we can actually temporarily add the combo to a placeholder list then immediately call editCombo on it to pull up an editing interface.
                # Then, when they exit editCombo, ask if they want to save the edited version or drop it entirely.
                temporary = [newcombo]
                editCombo(temporary, 0)
                # Re-save the edited version, and loop to ask again.
                newcombo = temporary[0]


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
        output = f"There are {len(combos)} combos saved."
        # Otherwise, iterate over all combos, generating a string for each
        for combo in combos:
            output += displayCombo(combo)
    # Display output
    while True:
        if (easygui.buttonbox(output, "All Combos - Combo Manager", ["Back to Menu", "Print to Shell"]) == "Print to Shell"):
            print(output)
            easygui.msgbox("The combos menu has been printed to the Python Shell.",
                           "All Combos - Combo Manager", "OK")
        else:
            return


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


# Print program information & show welcome screen
print("COMBO MANAGER")
print("Copyright (c) Conor Eager, 2021. All rights reserved.")
easygui.msgbox(
    "Welcome to Combo Manager!\nCopyright (c) Conor Eager, 2021. All rights reserved.\nFor more help and information, click [Help & About] on the main menu.", "Welcome - Combo Manager", "Continue to Main Menu")
# MAIN MENU
while True:
    # List of options:
    options = ["Add Combo", "View All", "Edit Combo",
               "Delete Combo", "Help & About", "Quit"]
    option = easygui.buttonbox(
        "Welcome to Combo Manager!\n\nSelect an action below.\nFor help and information, click [Help & About].\nTo exit this program, click [Quit].", "Main Menu - Combo Manager", options)
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
        # Show help.
        while True:
            item = easygui.choicebox("Select a help topic and press OK to view it, or press Cancel to go back to the main menu.",
                                     "Help & About - Combo Manager", list(help.keys()))
            if (item == None):
                # Cancel pressed - break to menu
                break
            else:
                easygui.msgbox(help[item], item, "Back")
    elif (option == options[5]):
        # Quit.
        if (easygui.ynbox("Are you sure you want to quit Combo Manager?", "Quit - Combo Manager", ["No, do not quit", "Yes, quit"]) == 0):
            # Yes, quit.
            exit()
        else:
            # No, do not quit.
            pass
