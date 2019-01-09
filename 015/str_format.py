#!/usr/bin/env python
# -*- coding:utf-8 -*-

# format 的位置参数
print("{0} love {1}.{2}".format('I', "Alisa", "imeixi" ))

# format的关键字参数
print("{a} love {b}.{c}".format(a = 'I', b = "Alisa", c = "imeixi" ))

# format的位置 + 关键字参数
# 位置参数必须在关键字参数之前
print("{0} love {b}.{c}".format('I', b = "Alisa", c = "imeixi" ))

# {{}} 花括号扩起来花括号，代表不转义该字符，就不作为位置参数
print("{{0}}".format('不打印'))

#
print("{0:.1f}{1}".format(27.658, 'GB'))

# 格式化ASCII 码
print('%c' % 97)
print('%c %c %c' % (97, 98, 99))

print('%s' % "hello, world")
print('%d + %d = %d' % (4, 5, 4 + 5))

print('%o' % 10)
print('%x' % 10)
print('%X' % 10)
print('%X' % 160)

print('%f' % 27.658)  # 默认小数点后保留6位
print('%e' % 27.658)
print('%E' % 27.658)
print('%g' % 27.658)
print('%G' % 27.658)
