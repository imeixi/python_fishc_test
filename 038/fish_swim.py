#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fishs import *

fish = Fish()
fish.move()
fish.move()
fish.move()

goldfish = Goldfish()
goldfish.move()
goldfish.move()

shark = Shark()
shark.eat()
shark.eat()

# Fish.__init__(shark)
shark.move()