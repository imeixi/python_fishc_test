#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

print("系统最大递归深度", sys.getrecursionlimit())


# 阶乘--递归
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


# 阶乘-- 迭代
def factorial1(n):
    result1 = n
    for i in range(1, n):
        result1 *= i
    return result1


number = int(input("请输入一个正整数："))
while number != 0:
    result = factorial1(number)
    print("%d 的阶乘是 %d (通过迭代实现)" % (number, result))

    result = factorial1(number)
    print("%d 的阶乘是 %d (通过递归实现)" % (number, result))

    number = int(input("请输入一个正整数："))




