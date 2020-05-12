#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
import turtle

t = turtle.Turtle()


def drawSpiral(t, lineLen):
    # 最小规模，0直接退出
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        # 减小规模，边长减5
        drawSpiral(t, lineLen - 5)


drawSpiral(t, 100)

turtle.done()
