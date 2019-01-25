#!/usr/bin/env python
# -*- coding:utf-8 -*-


class C:
    def __getattribute__(self, item):
        print("当该类的属性被访问时的行为,调用__getattribute__")
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print("当用户试图获取一个不存在的属性时,调用__getattr____")

    def __setattr__(self, key, value):
        print("调用__setattr__")
        super().__setattr__(key, value)

    def __delattr__(self, item):
        print("调用__delattr__")
        super().__delattr__(item)


# 当用户获取一个不存在的属性时
c = C()
print(c.x)
print("-------------------------------")

# 当用户给属性赋值时
c.x = 1
# 当用户访问一个存在的属性时
print(c.x)
print("-------------------------------")

# 当用户删除一个对象属性的时候
del c.x
print("-------------------------------")

print(c.x)

print("============================================")
getattr(c, "x", "如果属性不存在，打印这段话")
setattr(c, "x", 10)
getattr(c, "x", "如果属性存在，打印值")
delattr(c, "x")
