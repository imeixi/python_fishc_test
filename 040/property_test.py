#!/usr/bin/env python
# -*- coding:utf-8 -*-


class C(object):
    def __init__(self):
        self._x = 0

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")


c1 = C()
print(c1.x)

c1.x = 20
print(c1.x)

c1.x = 30
print(c1.x)