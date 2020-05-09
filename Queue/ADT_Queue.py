#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang


class Queue:
    def __init__(self):
        self.items = []

    # 测试是否空队列，返回值为布尔值
    def isEmpty(self):
        return self.items == []

    # 将数据项items添加至队尾，无返回值，复杂度为O(n)
    def enqueue(self, item):
        self.items.insert(0, item)

    # 从队首移除数据项，返回值为队首数据，队列被修改，复杂度为O(1)
    def dequeue(self, item):
        return self.items.pop()

    # 返回队列中数据项的个数
    def size(self):
        return len(self.items)


"""
如果首尾倒过来，复杂度也倒过来
"""