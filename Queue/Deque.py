#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang


class Deque:
    def __init__(self):
        self.items = []

    # 返回deque是否为空
    def isEmpty(self):
        return self.items == []

    # 将item加入队首，复杂度O(1)
    def addFront(self, item):
        self.items.append(item)

    # 将item加入队尾，复杂度O(n)
    def addRear(self, item):
        self.items.insert(0, item)

    # 从队首移除数据项，返回值为移除的数据项，复杂度O(1)
    def removeFont(self):
        return self.items.pop()

    # 从队尾移除数据项，返回值为移除的数据项，复杂度O(n)
    def removeRear(self):
        return self.items.pop(0)

    # 返回deque中包含数据项的个数
    def size(self):
        return len(self.items)
