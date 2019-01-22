#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 当过滤函数第一个参数为None时，将第二个参数中所有false的元素被过滤掉，只留下为True的变量
result = filter(None, [1, 0, None, True])
print(list(result))

# 当过滤函数第一个参数为一个函数时，将第二个容器中的所有元素都带入到第一个函数中，结果为false的元素被过滤掉，只留下为True的变量
result = filter(lambda x: x % 2, range(10))
print(list(result))