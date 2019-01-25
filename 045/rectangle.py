#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Rectangle:
    def __init__(self, weight=0, height=0):
        self.weight = weight
        self.height = height

    def __setattr__(self, key, value):
        if key == "square":
            self.weight = value
            self.height = value
        else:
            super().__setattr__(key, value)
            # self.__dict__[key] = value         # 推荐使用 super() 基类的方法

    def getArea(self):
        return self.weight * self.height


r = Rectangle(4, 5)
print(r.getArea())

r.square = 10
print(r.getArea())
