#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1、因为 str 对象是不可修改的
2、Capstr 作为子类 如果不重写 __new__() 方法 将不能够对传入的参数进行修改
3、修改参数后，调用父类 str的方法 创建类的对象
"""


class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


c = CapStr("I love this world!")
print(c)