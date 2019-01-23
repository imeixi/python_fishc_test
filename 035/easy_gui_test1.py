#!/usr/bin/env python
# -*- coding:utf-8 -*-

from easygui import *

chocices = ["Yes", "No", "Only on Friday"]
reply = choicebox("Do you like to eat fish?", choices=chocices)

msgbox("Backup complete!", ok_button="Good job!")

btn = buttonbox(msg='HH', title='TT ', choices=('Button1', 'Button2', 'Button3'), image=None)

print(btn)