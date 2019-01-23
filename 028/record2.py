#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open("record2.txt")
boy = []
girl = []
count = 1


def save_file(boy, girl, count):
    file_boy = "boy_" + str(count) + ".txt"
    file_girl = "girl_" + str(count) + ".txt"
    fb = open(file_boy, "w")
    fg = open(file_girl, "w")
    fb.writelines(boy)
    fg.writelines(girl)
    fb.close()
    fg.close()


for each in f:
    if each[:6] != "======":
        #分割字符
        (role, dialogue) = each.split(":")
        if role == "小甲鱼":
            boy.append(dialogue)
        else:
            girl.append(dialogue)
    else:
        #保存文件
        save_file(boy, girl, count)

        boy = []
        girl = []
        count += 1

save_file(boy, girl, count)

f.close()