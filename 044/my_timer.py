#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time


class MyTimer(int):
    def __init__(self):
        self.prompt = "请先调用start启动计时。。。"
        self.unit = ["年", "月", "日", "时", "分", "秒"]
        self.weight = [1, 12, 30, 24, 60, 60]
        self.begin = []
        self.end = []
        self.latest = []

    def start(self):
        self.begin = time.localtime()
        self.prompt = "请先调用stop停止计时"
        print("开始计时。。。")

    def stop(self):
        self.end = time.localtime()
        self.prompt = "总共运行"
        self._calc()
        for index in range(6):
            if self.latest[index]:
                self.prompt += str(self.latest[index]) + self.unit[index]
        print(self.prompt)

    def _calc(self):
        borrow = false
        for index in range(5, -1, -1):
            result = self.end[index] - self.begin[index]
            if borrow:
                result -= 1
            if result < 0:
                borrow = true
                result += self.weight[index]
            self.latest.insert(0, result)


t = MyTimer()
t.start()
t.stop()
