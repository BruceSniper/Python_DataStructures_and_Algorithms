#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
希尔排序
对无序表进行“间隔”划分子表，每个子列表都执行插入排序
复杂度约为O(n^3/2)
"""


def shellSort(alist):
    # 间隔设定
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            # 子列表排序
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount, "The list is", alist)
        # 间隔缩小
        sublistcount //= 2
    return alist


def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentValue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentValue


alist = [89, 67, 56, 45, 34, 23, 1]
shellSort(alist)
# print(alist)
