#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
栈顶尾端版本，push/pop 的复杂度为 O(1)
"""


class Stack:
    def __init__(self):
        self.items = []

    # 返回栈是否为空栈
    def isEmpty(self):
        return self.items == []

    # 将 item 加入栈顶，无返回值
    def push(self, item):
        self.items.append(item)

    # 将栈顶数据项移除并返回，栈被修改
    def pop(self):
        return self.items.pop()

    # “窥视”栈顶数据项，返回栈顶的数据项但不移除，栈不被修改
    def peek(self):
        return self.items[len(self.items)-1]

    # 返回栈中有多少个数据项
    def size(self):
        return len(self.items)
