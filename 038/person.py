#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Person:
    __age = 18

    def get_age(self):
        return self.__age

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


p = Person("AA", "male")
print(p.get_age())
# print(p.__age)

print(p._Person__age)
