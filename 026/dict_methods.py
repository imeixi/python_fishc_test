#!/usr/bin/env python
# -*- coding:utf-8 -*-

# fromkeys 默认有两个参数，第一个参数是所有的key，第二个参数要赋值给的value 第二个参数默认为None
# 创建 {1: None, 2: None, 3: None}
dict1 = dict.fromkeys((1, 2, 3))
print(dict1)

# fromkeys 默认有两个参数，第一个参数是所有的key，第二个参数的value 将赋值给所有的key
# {1: 'number', 2: 'number', 3: 'number'}
dict2 = dict1.fromkeys((1, 2, 3), "number")
print(dict2)

# fromkeys 默认有两个参数，第一个参数是所有的key，第二个参数的如果传人多个value 将作为一个元组赋值给所有的key
# {1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}
dict3 = dict1.fromkeys((1, 2, 3), ("one", "two", "three"))
print(dict3)

# fromkeys 默认有两个参数，只会赋值指定dict中的key，创建新的dict，并不改变原来的dict
dict4 = dict1.fromkeys((1, 3), "数字")
print(dict4)

# keys(), values(), items()
dict5 = dict.fromkeys(range(32), "赞")
print(dict5)

for each_key in dict5.keys():
    print(each_key)

for each_value in dict5.values():
    print(each_value)

for each_item in dict5.items():
    print(each_item)

print("dict5.get(32):", dict5.get(32))

print("32 in dict5:", 32 in dict5)
print("32 not in dict5:", 32 not in dict5)

dict5.clear()
print(dict5)

print(dict3)
dict3.pop(3)
print(dict3)

dict3.popitem()
print(dict3)

dict6 = dict2.copy()
print(dict6)

