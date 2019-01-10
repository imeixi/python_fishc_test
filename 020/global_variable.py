#!/usr/bin/env python
# -*- coding:utf-8 -*-


def change_variable():
    g_variable = 50
    print("修改内部参数1:" + str(g_variable))


def change_global_variable():
    global g_variable
    g_variable = 30
    print("修改内部参数2:" + str(g_variable))


# 全局变量
g_variable = 100
print("外部参数:" + str(g_variable))

change_variable()
print("外部参数:" + str(g_variable))

change_global_variable()
print("外部参数:" + str(g_variable))
