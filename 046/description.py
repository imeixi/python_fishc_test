#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MyDescriptor:
    def __init__(self):
        self.x = None

    def __get__(self, instance, owner):
        print("__get__, self = %s, instance = %s, owner = %s" % (self, instance, owner))
        return self.x

    def __set__(self, instance, value):
        print("__set__, self = %s, instance = %s, value = %s" % (self, instance, value))
        self.x = value

    def __delete__(self, instance):
        print("__delete__, self = %s, instance = %s" % (self, instance))


class Test:
    x = MyDescriptor()


test = Test()
test.x
print(test)
print(Test)

print("------------------------------------------")
test.x = "Superman"
print(test.x)

# del test.x