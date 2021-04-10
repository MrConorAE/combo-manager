# Combo Manager
# Copyright (c) Conor Eager, 2021. All rights reserved.

# IMPORTS
# Import EasyGUI for the graphical interface.
import easygui
# Import Pickle for saving and loading combos.
import pickle

# DATA STORAGE
# Defining the global variables and data structures used.


class Combo(name, items):
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