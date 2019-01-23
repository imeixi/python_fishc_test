#!/usr/bin/env python
# -*- coding:utf-8 -*-

try:
    with open("1.txt", "w") as f:
        for each in f:
            print(each)
except OSError as reason:
    print("出错了。。" + str(reason))