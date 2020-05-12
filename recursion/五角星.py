#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
import turtle

t = turtle.Turtle()

t.pencolor('red')
t.pensize(3)

for i in range(5):
    t.forward(100)
    t.right(144)
t.hideturtle()

turtle.done()
