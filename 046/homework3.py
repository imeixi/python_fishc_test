#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time as t

class Record:
    def __init__(self, value, name):
        self.val = value
        self.name = name

    def __get__(self, instance, owner):
        local_time = t.localtime()
        record_time = t.strftime("%c", local_time)
        with open("record.txt", "a") as f:
            f.write("%s 变量与北京时间 %s 被读取，%s = %s\n" % (self.name, str(record_time), self.name, str(self.val)))
        return self.val

    def __set__(self, instance, value):
        self.val = value
        with open("record.txt", "a") as f:
            f.write("%s 变量与北京时间 %s 被修改，%s = %s\n" % (self.name, t.ctime(), self.name, str(value)))


class Test:
    x = Record(10, 'x')
    y = Record(8.8, 'y')


test = Test()
print(test.x)
print(test.y)

test.x = 123
test.x = 1.23
test.y = "I love the word"



