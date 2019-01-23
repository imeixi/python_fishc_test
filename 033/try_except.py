#!/usr/bin/env python
# -*- coding:utf-8 -*-

try:
    int("abc")
    sum = 1 + "1"                     # typeError 捕获
    f = open("I am not exist")        # OSError 捕获
    print(f.read())
    f.close()

except OSError as reason:
    print("文件出错啦T_T\n错误原因是：" + str(reason))

except TypeError as reason:
    print("类型出错啦T_T\n错误原因是：" + str(reason))

except:                     # 不建议使用
    print("出错了。。")