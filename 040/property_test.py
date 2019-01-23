#!/usr/bin/env python
# -*- coding:utf-8 -*-


class C(object):
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")


c1 = C()

c1.x = 20
print(c1.x)

del c1.x
print(c1.x)