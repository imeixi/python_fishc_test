#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Fish:
    def __init__(self, x):
        self.num = x


class Turtle:
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def summary(self):
        print("The pool have %d turtles and %d fishes." % (self.turtle.num, self.fish.num))


pool = Pool(1, 10)
pool.summary()
