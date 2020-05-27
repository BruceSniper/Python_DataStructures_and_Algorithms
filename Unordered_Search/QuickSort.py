#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
快速排序
如果分裂总能把数据表分为相等的两部分，那么
就是O(log n)的复杂度；
而移动需要将每项都与中值进行比对，还是O(n)
综合起来就是O(nlog n)
"""


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)


def quickSortHelper(alist, first, last):
    # 基本结束条件
    if first < last:
        splitpoint = partition(alist, first, last)      # 分裂
        # 递归调用
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
    # 选定中值
    pivotvalue = alist[first]
    # 左右标初值
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        # 向右移动左标
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        # 向左移动右标
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        # 两标相错就结束移动
        if rightmark < leftmark:
            done = True
        else:
            # 左右标的值交换
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    # 中值就位
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)
