#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random as r


class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("我的位置：", self.x, self.y)


class Goldfish(Fish):
    pass


class Carp(Fish):
    pass


class Salmon(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)          # 调用未绑定的父类的方法
        super().__init__()             # 使用super函数
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("It's delicious")
            self.hungry = False
        else:
            print("I am full")