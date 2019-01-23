#!/usr/bin/env python
# -*- coding:utf-8 -*-

import easygui as g

g.msgbox("Danger, Will Robinson!", "Warning!")

msg = "Do you want to continue?"
title = "Please Confirm"
if g.ccbox(msg, title):
    g.msgbox("you will be win")
else:
    g.msgbox("See you")
