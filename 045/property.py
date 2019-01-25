#!/usr/bin/env python
# -*- coding:utf-8 -*-


class C:
    def __init__(self, size=10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize)


c = C()
print(c.x)
print(c.size)

c.x = 100
print(c.size)

print(getattr(c, "y", "不存在的属性"))
print(getattr(c, "x", "不存在的属性"))
setattr(c, "x", 900)
print(getattr(c, "x", "不存在的属性"))
