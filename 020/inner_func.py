#!/usr/bin/env python
# -*- coding:utf-8 -*-


def func1():
    print("func1 正在被调用......")

    def func2():
        print("func2 正在被调用 ......")

    func2()


# 调用函数
func1()