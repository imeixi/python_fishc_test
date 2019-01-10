#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
整个文件的doc解释文档
"""


# 定义一个函数
def my_first_function(name):
    """函数定义中的解释文档，与注释不同，可通过函数的__doc__属性查看"""
    print("这是我创建的第一个函数")
    print("I am very excited.")
    print(name + "you will be stronger and stronger")


# 调用一个函数
my_first_function("zah")

# 查看文档的第一种方式
print("查看文档的第一种方式 : my_first_function.__doc__")
print(my_first_function.__doc__)

# 查看文档的第二种方式
print("\n查看文档的第二种方式 : help(my_first_function)")
help(my_first_function)


