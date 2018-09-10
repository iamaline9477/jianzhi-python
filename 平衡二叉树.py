#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

思路：
平衡二叉树：空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:#空树是平衡二叉树
            return True
        left=self.IsBalanced_Solution(pRoot.left)
        right=self.IsBalanced_Solution(pRoot.right)
        if left==True and right==True and abs(self.depth(pRoot.left)-self.depth(pRoot.right))<=1:
            return True

    def depth(self,pRoot):
        if not pRoot:
            return 0
        left=self.depth(pRoot.left)
        right=self.depth(pRoot.right)
        if left>right:
            return left+1
        else:
            return right+1