#!/usr/bin/env python
# -*- coding:utf-8 -*-

user = 'zah'
name = "zhengaihua IMEIXI\t Alisa"
print(name)

# 首字母变大写
print(name.capitalize())

# 返回标题话，每个单词都以大写字母开头，其余是小写字母
print(name.title())

# 全部变小写
print(name.casefold())

# 将字符串居中，并使用空格填充至长度 width 的新字符串,第二个参数表示用什么字符填充，默认是空格
print(name.center(40))
print(name.center(40, "*"))

# 将字符串左对齐，并使用空格填充至长度 width 的新字符串,第二个参数表示用什么字符填充，默认是空格
print(name.ljust(40))
print(name.ljust(40, '*'))

# 统计字符串出现的次数  用法等同于List
print(name.count('ai'))

# 判断是否以制定字符串结尾
print(name.endswith('isa'))
print(name.endswith('is'))
# 判断是否以制定字符串开头
print(name.startswith('isa'))
print(name.startswith('is'))

# 把字符串中的 tab 符号（\t）转换为空格，如不指定参数，默认的空格数是 tabsize=8。
print(name.expandtabs())
print(name.expandtabs(32))

# 检测 sub 是否包含在字符串中，如果有则返回索引值，否则返回 -1，start 和 end 参数表示范围，可选。
print(name.find('MEIXI'))
print(name.find('sea'))

# 跟 find 方法一样，不过如果 sub 不在 string 中会产生一个异常。
print(name.index("Alisa"))
# print(name.index("sea"))   如果找不到会报错

str_1 = '123'
print(str_1.isalnum())
print(str_1.isalpha())
print(str_1.isdecimal())
print(str_1.isdigit())
print(str_1.islower())
print(str_1.isupper())
print(str_1.isnumeric())
print(str_1.isspace())
print(str_1.istitle())

# 以字符串作为分隔符，插入到 sub 中所有的字符之间。
print(str_1.join(user))

print(name.lower())
print(name.upper())
print(name.swapcase())  # 翻转字符串中的大小写


print(name.lstrip())   #去掉字符串左边的空格
print(name.rstrip())   #去掉字符串末尾的空格
print(name.strip())    #去掉字符串前后的空格
print(name.strip('s'))    #去掉字符串前后的空格

# 找到子字符串 sub，把字符串分成一个 3 元组 (pre_sub, sub, fol_sub)，如果字符串中不包含 sub 则返回 ('原字符串', '', '')
print(name.partition('IMEIXI'))

# 替换
print(name.replace('sa', 'SA'))

# 从右侧开始。。。
print(name.rfind("sa"))
print(name.rindex("sa"))
print(name.rjust(40))
print(name.rpartition("IMEIXI"))
print(name.rstrip())

# 按制定字符分割，默认按空格分割
print(name.split())
print(name.split("i"))

# 按 \n 分割
print(name.splitlines())

# 根据 table 的规则（可以由 str.maketrans('a', 'b') 定制）转换字符串中的字符。
print(name.translate(str.maketrans('i', 'a')))

# 返回长度为 width 的字符串，原字符串右对齐，前边用 0 填充。
print(name.zfill(60))


