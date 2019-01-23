#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
https://easygui.readthedocs.io/en/latest/tutorial.html
"""

from easygui import read_or_create_settings

# Create the settings object.
settings = read_or_create_settings('settings1.txt')

# Save the variables as attributes of the "settings" object
settings.userId = "obama_barak"
settings.targetServer = "whitehouse1"
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