#!/usr/bin/env python
# -*- coding:utf-8 -*-

domain = "IMEIXI"

for i in domain:
    print(i, end=" ")

print('\n')
members = ['Audi', 'Volvo', 'Volkswagen', "Mercedes"]
for auto in members:
    print(auto, len(auto))


for i in range(5):
    print(i)

print('\n')
for i in range(7, 10):
    print(i)

print('\n')
for i in range(1, 10, 2):
    print(i)

# continue
print('\n')
for i in range(10):
    if i % 2 == 0:
        print(i)
        continue
    i += 2
    print(i)
