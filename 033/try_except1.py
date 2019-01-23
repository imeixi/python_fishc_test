#!/usr/bin/env python
# -*- coding:utf-8 -*-

try:
    f = open("I am exist", "w")        # OSError 捕获
    print(f.write("我存在了"))
    sum = 1 + "1"                     # typeError 捕获
except (OSError, TypeError):
    print("文件出错啦T_T")
finally:
    f.close()
