#!/usr/bin/env python
# -*- coding:utf-8 -*-

s = {1, 2, 3, 4, 5}
t = {1, 2, 3, 6, 7}
n = {1, 2}

print(t.issubset(s))
print(n.issubset(s))

print(s.issuperset(t))
print(s.issuperset(n))

print(s.union(t))
print(s.intersection(t))

print(s.difference(t))
print(s.symmetric_difference(t))

s.update(t)
print(s)

s = {1, 2, 3, 4, 5}
s.intersection_update(t)
print(s)

s = {1, 2, 3, 4, 5}
s.difference_update(t)
print(s)

s = {1, 2, 3, 4, 5}
s.symmetric_difference_update(t)
print(s)

s.add(0)
print(s)

s.remove(0)
print(s)

s.discard(10)
print(s)

s.discard(1)
print(s)

s.pop()
print(s)

s.clear()
print(s)
