#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
二叉堆

堆排序算法复杂度：O(nlogn)
"""


class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def perUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                # 与父节点交换
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            # 沿路径向上
            i = i // 2

    def insert(self, k):
        # 添加到末尾
        self.heapList.append(k)
        self.currentSize += 1
        # 新key上浮
        self.perUp(self.currentSize)

    def perDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                # 交换下沉
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            # 沿路径向下
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            # 唯一子节点
            return i * 2
        else:
            # 返回较小的
            if self.heapList[i * 2] < self.heapList[i * 2 - 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        # 移走堆项
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        # 新顶下沉
        self.perDown(1)
        return retval

    def buildHeap(self, alist):
        # 从最后的父节点开始，因叶节点无需下沉
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)
        while i > 0:
            print(self.heapList, i)
            self.perDown(i)
            i -= 1
        print(self.heapList, i)
