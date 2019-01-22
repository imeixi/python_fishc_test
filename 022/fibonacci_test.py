#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time


# 递归
def fibonacci(n):
    if n < 1:
        print("输入有误！")
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# 迭代
def fib(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print("输入有误！")
        return -1

    while (n-2) > 0:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1

    return n3


# 调用
t1 = time.time()
# n = int(input("please input one Integer Number:"))
result = fib(35)
print("迭代方式计算结果为：%d" % result)
t2 = time.time()
print("迭代方法用时：%f" % float(t2 - t1))

t1 = time.time()
result2 = fibonacci(35)
print("递归方式计算结果为：", result2)
t2 = time.time()
print("递归方法用时：%f" % float(t2 - t1))

