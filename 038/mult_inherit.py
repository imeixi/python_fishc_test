#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Base1:
    def foo1(self):
        print("I am foo1")


class Base2:
    def foo2(self):
        print("I am foo2")


class CC(Base1, Base2):
    pass


c = CC()
c.foo1()
c.foo2()
