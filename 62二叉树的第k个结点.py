#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。

思路：
对于二叉搜索树，中序遍历即为从小到大的排序'''


class Solution:
    def __init__(self):
        self.stack = []

    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot or k <= 0:
            return None
        self.mid(pRoot)
        if k > len(self.stack):
            return None
        return self.stack[k - 1]

    def mid(self, pRoot):
        if not pRoot:
            return None
        self.mid(pRoot.left)
        self.stack.append(pRoot)
        self.mid(pRoot.right)
