#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

思路：
二叉搜索树：左子树all小于根，右子树all大于根，子树也是二叉搜索树
后序遍历：左子树-右子树-根
如：	     5
    	   /  \
    	  3    7
    	 / \  / \
    	1  4 6  8
后序遍历为[1,4,3,6,8,7,5]
可见数组中除了最后一位（根）可以分为两个子数组：左子树（小于根），右子树（大于根），
并且这两个子数组也是后序遍历得到的结果（递归）。
故我们先寻找第一个大于根的位置，若此位置后有小于根的数，直接返回false
若无则判断左右子树是否后序，需要考虑左右子树为空的情况'''



class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        for i in range(len(sequence)):
            if sequence[i] > sequence[-1]:
                break
        for num in sequence[i:-1]:
            if num < sequence[-1]:
                return False
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        right = True
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right