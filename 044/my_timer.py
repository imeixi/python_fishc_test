#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time


class MyTimer(int):
    def __init__(self):
        self.prompt = "尚未开始计时。。。"
        self.unit = ["年", "月", "日", "时", "分", "秒"]
        self.weight = [1, 12, 30, 24, 60, 60]
        self.begin = 0
        self.end = 0
        self.latest = []

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        prompt = "总共运行了"
        summary = []
        carry = False
        for index in range(5, -1, -1):
            result = self.latest[index] + other.latest[index]
            if carry:
                result += 1
                carry = False
            if result >= self.weight[index]:
                carry = True
                result -= self.weight[index]
            summary.insert(0, result)

        for index in range(6):
            if summary[index]:
                prompt += str(summary[index]) + self.unit[index]
        return prompt

    def start(self):
        if not self.begin:
            self.begin = time.localtime()
            self.prompt = "请先调用stop停止计时"
            print("开始计时。。。")
            print("begin = ", self.begin)
        else:
            print("正在计时中。。。")

    def stop(self):
        if not self.begin:
            print("请先开始计时。。。")
        else:
            self.end = time.localtime()
            print("end = ", self.end)
            self._calc()
            print("计时结束。。。")

    def _calc(self):
        self.prompt = "总共运行"

        borrow = False
        for index in range(5, -1, -1):
            result = self.end[index] - self.begin[index]
            if borrow:
                result -= 1
                borrow = False
            if result < 0:
                borrow = True
                result += self.weight[index]
            self.latest.insert(0, result)

        for index in range(6):
            if self.latest[index]:
                self.prompt += str(self.latest[index]) + self.unit[index]

        self.begin = 0
        self.end = 0


t1 = MyTimer()
t1.start()
time.sleep(61)
t1.stop()
print(t1)

t2 = MyTimer()
t2.start()
time.sleep(59)
t2.stop()
print(t2)
print(t1 + t2)