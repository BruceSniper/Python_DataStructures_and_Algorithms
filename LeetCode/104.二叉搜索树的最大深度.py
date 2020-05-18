#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang


class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solition(object):
    def maxDepth(self, root: TreeNode) -> int:
        """
        :type root:  TreeNode
        :rtype: int
        """
        # 上面未提及如果根节点直接为空， 无需遍历，返回0
        if root is None:
            return 0
        # count1, count2 = 0, 0
        # # 当前根节点的左子树是否为空
        # if root.left is not None:
        #     count1 += self.maxDepth(root.left) + 1
        # # 当前根节点的右子树是否为空
        # if root.right is not None:
        #     count2 += self.maxDepth(root.right) + 1
        # # 当前节点为叶节点时，返回深度 1
        # if root.left is None and root.right is None:
        #     return 1
        # return max(count1, count2)
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height)+1
