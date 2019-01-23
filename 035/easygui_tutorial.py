#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
https://easygui.readthedocs.io/en/latest/tutorial.html
"""

from easygui import EgStore

# -----------------------------------------------------------------------
# define a class named Settings as a subclass of EgStore
# -----------------------------------------------------------------------
class Settings(EgStore):

    def __init__(self, filename):  # filename is required
        # -------------------------------------------------
        # Specify default/initial values for variables that
        # this particular application wants to remember.
        # -------------------------------------------------
        self.userId = ""
        self.targetServer = ""

        # -------------------------------------------------
        # For subclasses of EgStore, these must be
        # the last two statements in  __init__
        # -------------------------------------------------
        self.filename = filename  # this is required
        self.restore()

# Create the settings object.
# If the settingsFile exists, this will restore its values
# from the settingsFile.
# create "settings", a persistent Settings object
# Note that the "filename" argument is required.
# The directory for the persistent file must already exist.

settingsFilename = "settings.txt"
settings = Settings(settingsFilename)

# Now use the settings object.
# Initialize the "user" and "server" variables
# In a real application, we'd probably have the user enter them via enterbox
user    = "obama_barak"
server  = "whitehouse1"

# Save the variables as attributes of the "settings" object
settings.userId = user
settings.targetServer = server
settings.store()    # persist the settings
print("\nInitial settings")
print(settings)

# Run code that gets a new value for userId
# then persist the settings with the new value
user    = "biden_joe"
settings.userId = user
settings.store()
print("\nSettings after modification")
print(settings)

# Delete setting variable
del settings.userId
print("\nSettings after deletion of userId")
print(settings)
