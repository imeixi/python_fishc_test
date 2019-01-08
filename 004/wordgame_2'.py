#!/usr/bin/env python
# -*- coding:utf-8 -*-

# !/usr/bin/env python
# -*- coding:utf-8 -*-

import random

secret = random.randint(1, 10)
print("-----------第一个文本小游戏------------")
temp = input("输入你想到的数字:")
guess = int(temp)
i = 0
while guess != secret and i < 2:
    if guess > secret:
        print("your num is bigger than mine")
    else:
        print("your num is smaller than mine")

    i = i + 1
    temp = input("输入你想到的数字:")
    guess = int(temp)

if guess == secret:
    print("this is my number, you have me")
    print("I love this number")
else:
    print("you have no chance, my word is ", secret)


print("Game Over")
