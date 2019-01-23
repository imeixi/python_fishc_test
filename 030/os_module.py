#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

# os.getcwd()
# os.chdir()
# os.listdir()
# os.mkdir()
# os.system()

for root, dirs, files in os.walk("/Users/zhengaihua/aa"):
    print("root= ", root)
    print("dirs= ", dirs)
    print("files= ", files)
print('..................................................')

