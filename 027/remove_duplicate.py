#!/usr/bin/env python
# -*- coding:utf-8 -*-

# remove_duplicate
num = [1, 2, 3, 4, 5, 5, 3, 1, 0]
num1 = [1, 2, 3, 4, 5, 5, 3, 1, 0]

# method I:
temp = []

for each in num1:
    if each not in temp:
        temp.append(each)

print(temp)

# method II:
for each_num in num:
    if num.count(each_num) > 1:
        num.remove(each_num)

print(num)

# method III
print(list(set(num1)))