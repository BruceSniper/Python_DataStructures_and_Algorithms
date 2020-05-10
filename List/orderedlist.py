#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
from .node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    # 在表中添加一个数据项，并保持整体顺序，此项原不存在，复杂度O(n)，平均操作次数n/2
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    # 从有序表中移除一个数据项，此项应存在，有序表被修改，复杂度O(n)，平均操作次数n/2
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    # 有序表中查询找数据项，返回是否存在，复杂度O(n)，平均操作次数n/2
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    # 是否空表，复杂度O(1)
    def isEmpty(self):
        return self.head is None

    # 返回表中数据项的个数，复杂度O(n)
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    # 返回数据项在表中的位置，此项应存在
    def index(self, item):
        pass

    # 移除并返回有序表的最后一项，表中应至少存在一项
    def pop(self):
        pass

    # 移除并返回有序表中指定位置的数据项，此位置应该存在
    def pop_pos(self, pos):
        pass
