#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一颗二叉树的根节点和一个整数，
打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)

思路：
如果只有根节点or找到叶子节点，把对应val返回
如果不是叶子节点，分别对根节点的左子树、右子树进行递归，直到找到叶子结点。
然后遍历把叶子结点和父节点对应的val组成的序列返回上一层；
没找到路径时也返回了序列[]'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        result = []
        if not root:
            return result
        if root.left == None and root.right == None and root.val == expectNumber:
            return [[root.val]]
        else:
            left = self.FindPath(root.left, expectNumber - root.val)
            right = self.FindPath(root.right, expectNumber - root.val)
            for n in left + right:
                result.append([root.val] + n)
        return result

