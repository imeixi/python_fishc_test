#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pickle as p
import os


class MyDes:

    # 已保存的参数名称
    saved = []

    def __init__(self, name=None):
        self.name = name
        self.path = self.name + '.pkl'

    def __get__(self, instance, owner):
        if self.name not in MyDes.saved:
            raise AttributeError("%s 属性还没有赋值！" % self.name)

        with open(self.path, "rb") as f:
            val = p.load(f)

        return val

    def __set__(self, instance, value):
        with open(self.path, "wb") as f:
            p.dump(value, f)
            MyDes.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.path)
        MyDes.saved.remove(self.name)


class Test:
    x = MyDes('x')
    y = MyDes('y')


test = Test()
test.x = 123
test.y = "I love the world"
print(test.x)
print(test.y)
del test.x