#!/usr/bin/env python
# -*- coding:utf-8 -*-

print("-----------第一个文本小游戏------------")
temp = input("输入你想到的数字:")
guess = int(temp)
if guess == 8:
    print("this is my number, you have me")
    print("I love this number")
else:
    print("Sorry, you are wrong ,I like 8")
print("Game Over")
