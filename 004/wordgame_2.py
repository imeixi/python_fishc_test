#!/usr/bin/env python
# -*- coding:utf-8 -*-

print("-----------第一个文本小游戏------------")
temp = input("输入你想到的数字:")
guess = int(temp)
i = 0
while guess != 8 and i < 2:
    if guess > 8:
        print("your num is bigger than mine")
    else:
        print("your num is smaller than mine")

    i = i + 1
    temp = input("输入你想到的数字:")
    guess = int(temp)

if guess == 8:
    print("this is my number, you have me")
    print("I love this number")
else:
    print("you have no chance")


print("Game Over")
