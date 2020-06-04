#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
表达式解析树
"""
from Stack.ADT_Stack_Top import Stack
from .BinaryTree_use_list import BinaryTree


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    # 入栈下降
    pStack.push(eTree)
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            # 入栈下降
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        # 操作数
        elif i not in ['+', '_', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            # 出栈上升
            parent = pStack.pop()
            currentTree = parent
        # 操作符
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        # 表达式结束
        elif i == ')':
            # 出栈上升
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree
