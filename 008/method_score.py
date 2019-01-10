#!/usr/bin/env python
# -*- coding:utf-8 -*-

score = int(input("please input a score:"))

if score > 100:
    print("please input a score less than 100")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("It's bad")