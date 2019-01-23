#!/usr/bin/env python
# -*- coding:utf-8 -*-

try:
    print(int("123"))
except ValueError as reason:
    print("出错啦。。。")
else:
    print("没有出现异常。。")