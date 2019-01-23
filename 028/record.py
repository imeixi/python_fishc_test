#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open("record.txt", "r")
fb = None
fg = None
n = 0

for each in f:
    if each.startswith("====="):
        if fb is not None and fg is not None:
            fb.close()
            fg.close()
        n += 1
        file_b = "boy_" + str(n) + ".txt"
        file_g = "girl_" + str(n) + ".txt"
        fb = open(file_b, "w")
        fg = open(file_g, "w")

    if each.startswith("小甲鱼:"):
        fb.write(each.replace("小甲鱼:", ""))

    if each.startswith("客服:"):
        fg.write(each.replace("客服:", ""))

fb.close()
fg.close()
f.close()

