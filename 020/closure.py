#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 如果在一个内部函数里，对在外部作用域的变量进行了引用，那么这个内部函数就被称为闭包。
def fun_x(x):
    """返回一个函数名，不加()"""
    def fun_y(y):
        return x * y
    return fun_y   #


# fun_y就是一个闭包
# 调用1,先返回一个函数
f = fun_x(8)
print(f)

result = f(5)
print(result)

# 调用2
print(fun_x(8)(10))


def fun1():
    """nonlocal 使内嵌函数引用外部变量 ----推荐 """
    x = 5

    def fun2():
        nonlocal x
        x *= x
        return x
    return fun2()


print(fun1())


def fun11():
    """ python2 使内嵌函数引用外部变量----不推荐 """
    x = [5]

    def fun2():
        x[0] *= x[0]
        return x[0]
    return fun2()


print("使用容器方式，在内嵌函数中调用外部函数变量" + fun11())
