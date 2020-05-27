#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
归并排序 Pythonic版

将归并排序分为两个过程来分析：分裂 和 归并

分裂的过程，借鉴二分查找中的分析结果，是对数复杂度，时间复杂度为O(log n)

归并的过程，相对于分裂的每个部分，其所有数据项都会被比较和放置一次，所以
是线性复杂度，其时间复杂度是O(n)

综合考虑，每次分裂的部分都进行一次O(n)的数据项归并，总的时间复杂度是O(nlog n)
"""


def merge_sort(lst):
    # 递归结束条件
    if len(lst) <= 1:
        return lst

    # 分解问题，并递归调用
    middle = len(lst)//2
    left = merge_sort(lst[:middle])     # 左半部排好序
    right = merge_sort(lst[middle:])    # 右半部排好序

    # 合并左右半部，完成排序
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged
