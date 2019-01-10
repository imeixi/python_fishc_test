#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 带参数的函数
def my_second_function(name):
    print(name + " Fighting!")


# Addition, subtraction, multiplication and division
def add(num1, num2):
    print(num1 + num2)


# 带返回值
def sub(num1, num2):
    return num1 - num2


def multi(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 is not 0:
        return num1 / num2
    else:
        return None
