#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。

思路：
中序遍历写入一个list，再改变list里元素的指针'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        self.lst = []
        self.midtraverse(pRootOfTree)
        for i in range(len(self.lst)):
            if i < len(self.lst) - 1:
                self.lst[i].right = self.lst[i + 1]
                self.lst[i + 1].left = self.lst[i]
        return self.lst[0]

    def midtraverse(self, Tree):
        if not Tree:
            return None
        self.midtraverse(Tree.left)
        self.lst.append(Tree)
        self.midtraverse(Tree.right)