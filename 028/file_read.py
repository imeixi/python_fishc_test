#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open("1.txt", "rb")
print(f)

print("当前文件指针所在位置:", f.tell())
s = f.read(10)
print("读取10个字节的内容：", s)
print("当前文件指针所在位置变为:", f.tell())

print("当前文件指针所在位置变为:", f.seek(5, 0))          # 使用seek 定位文件指针时，文件读取方式必须以二进制方式读取"b"
print("当前文件指针所在位置变为:", f.seek(5, 1))          # 否则，只允许 seek 从开头读取。
print("当前文件指针所在位置变为:", f.seek(-18, 2))

s = f.readline()
print("读取1行的内容：", s)

# 读取每行I
f.seek(0, 0)
lines = list(f)
for each in lines:
    print(each)

# 读取每行II
f.seek(0, 0)
for each_line in f:
    print(each_line)
