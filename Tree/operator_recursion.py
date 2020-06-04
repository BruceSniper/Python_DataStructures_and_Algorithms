#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
import operator
from .BinaryTree_use_list import BinaryTree


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    # 缩小规模
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        # 递归调用
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        # 基本结束条件
        return parseTree.getRootVal()