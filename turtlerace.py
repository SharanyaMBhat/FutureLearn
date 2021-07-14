#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 06:56:42 2021

@author: Sharanya
"""

from turtle import Turtle
from random import randint

laura = Turtle()
laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(-160,100)
laura.pendown()


rick = Turtle()
rick.color('green')
rick.shape('turtle')
rick.penup()
rick.goto(-160,70)
rick.pendown()


karen = Turtle()
karen.color('blue')
karen.shape('turtle')
karen.penup()
karen.goto(-160,40)
karen.pendown()

megahan = Turtle()
megahan.color('pink')
megahan.shape('turtle')
megahan.penup()
megahan.goto(-160,20)
megahan.pendown()

for movement in range(100):
    laura.forward(randint(1, 5))
    rick.forward(randint(1, 5))
    karen.forward(randint(1, 5))
    megahan.forward(randint(1, 5))