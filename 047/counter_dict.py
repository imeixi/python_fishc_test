#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
编写一个不可改变的自定义列表，要求记录列表中每个元素被访问的次数。
'''


class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]      # 列表推导式
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        self.count[item] += 1
        return self.values[item]

    def __setitem__(self, key, value):
        self.count[key] += 1
        self.values[key] = value

    def __delitem__(self, key):
        self.values.remove(self.values[key])
        self.count.pop(key)

    def counter(self, index):
        return self.count[index]


c1 = CountList(1, 3, 5, 7, 9)
c2 = CountList(2, 4, 6, 8, 10)
print(c1.count)
print(c2.count)

print(c1[1])
print(c1.count)

c1[2] + c2[2]
print(c1.count)

print(c2.count)

c1[1] = 22
print(c1.count)

del c1[2]
print(c1.values)
print(c1.count)
