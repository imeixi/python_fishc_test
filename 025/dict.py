#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 创建一个字典
dict1 = {1: "one", 2: "two", "3": "three"}
print(dict1[1])
print(dict1[2])
print(dict1["3"])

dict2 = dict((("A", 20), ("b", 30), ("C", 40)))
print(dict2)

dict3 = dict([("AA", 25), ("bb", 35), ("CC", 45)])
print(dict3)

dict3 = dict([("AA", 25), ("bb", 35), ("CC", 45)])
print(dict3)

# 使用key-value方式，创建dict，key不能加引号
dict4 = dict(姓名="name", 性别='male', 年龄='35')
print(dict4)


# 修改字典中的健的值，如果有直接修改，如果没有直接创建
dict4["姓名"] = "zhengaihua"
dict4["score"] = 100
print(dict4)
