#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 07:25:44 2021

@author: z0044c9
"""

from shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()

rect2 = Rectangle()
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")
rect2.set_x(100)
rect2.set_y(100)
rect2.draw()

triangle = Triangle()
triangle.randomize()
triangle.set_color("pink")
triangle.draw()

oval = Oval()
oval.randomize(30,60)
oval.set_x(150)
oval.set_y(250)
oval.draw()

paper.display()
