#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pickle

s = [1, 3.14, "xiao"]
file = open("pickle.pkl", "wb")
pickle.dump(s, file)
file.close()

pickle_file = open("pickle.pkl", "rb")
ss = pickle.load(pickle_file)
print(ss)