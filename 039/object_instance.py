#!/usr/bin/env python
# -*- coding:utf-8 -*-


class CC:
    def setXY(self, x, y):
        self.x = x
        self.y = y

    def printXY(self):
        print(self.x, self.y)


dd = CC()
print(CC.__dict__)
print(dd.__dict__)

dd.setXY(4, 5)
print(dd.__dict__)

del CC
dd.printXY()

ee = CC()