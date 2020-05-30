#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
树的嵌套列表实现
[root, left, right]
根是myTree[0]，左子树myTree[1]，右子树myTree[2]
"""


# 创建仅有根节点的二叉树
def BinaryTree(r):
    return [r, [], []]


# 将新节点插入树中作为其直接的左子节点
def insertLeft(root, newBranch):
    t =root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


# 将新节点插入树中作为其直接的右子节点
def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


# 返回根节点
def getRootVal(root):
    return root[0]


# 设置根节点的值
def setRootVal(root, newVal):
    root[0] = newVal


# 返回左子树
def getLeftChild(root):
    return root[1]


# 返回右子树
def getRightChild(root):
    return root[2]


r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
l = getLeftChild(r)
print(l)

setRootVal(l, 9)
print(r)

insertLeft(l, 11)
print(r)

print(getRightChild(getRightChild(r)))
