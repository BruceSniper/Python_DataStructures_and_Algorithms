#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
归并排序
将归并排序分为两个过程来分析：分裂 和 归并

分裂的过程，借鉴二分查找中的分析结果，是对数复杂度，时间复杂度为O(log n)

归并的过程，相对于分裂的每个部分，其所有数据项都会被比较和放置一次，所以
是线性复杂度，其时间复杂度是O(n)

综合考虑，每次分裂的部分都进行一次O(n)的数据项归并，总的时间复杂度是O(nlog n)
"""


def mergeSort(alist):
    # 结束基本条件
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # 递归调用
        mergeSort(lefthalf)
        mergeSort(righthalf)

        # 拉链式交错把左右半部从小大大归并到结果列表中
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        # 归并左半部剩余项
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        # 归并右半部剩余项
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1