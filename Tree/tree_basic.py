#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    # 前序遍历
    def preorder(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    # 中序遍历
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    # 后序遍历
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.val)
