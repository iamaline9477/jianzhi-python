#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
请实现两个函数，分别用来序列化和反序列化二叉树

思路：
序列化：按照某种遍历顺序存储，若为空则加入#
反序列化：将序列化的结果转为二叉树
这里采取的是前序'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.idx = -1

    def Serialize(self, root):
        if not root:
            return '#!,'
        return str(root.val) + ',' + self.Serialize(root.left) + self.Serialize(root.right)

    def Deserialize(self, s):
        if not s:
            return None
        self.idx += 1
        lst = s.split(',')
        if self.idx >= len(s):
            return None
        root = None
        if lst[self.idx] != '#!':
            root = TreeNode(int(lst[self.idx]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
