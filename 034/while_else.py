#!/usr/bin/env python
# -*- coding:utf-8 -*-


def show_max_factor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print("%d 的最大因数是：%d" % (num, count))
            break
        count -= 1
    else:
        print("%d 是素数" % num)


num = int(input("please input a number:"))
show_max_factor(num)