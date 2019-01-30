#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MyDes:
    def __init__(self, value=None, name=None):
        self.val = value
        self.name = name

    def __get__(self, instance, owner):
        print("正在获取变量：", self.name)
        return self.val

    def __set__(self, instance, value):
        print("正在修改变量：", self.name)
        self.val = value

    def __delete__(self, instance):
        print("正在删除变量：", self.name)
        print("哦，暂时无法删除。。。")


class Test:
    x = MyDes(10, "x")


if __name__ == "__main__":
    test = Test()
    y = test.x
    print(y)
    test.x = 8
    del test.x
    print(test.x)