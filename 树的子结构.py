#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）

思路：
首先在树A中找到和树B根节点值相同的节点R；
然后判断树A中以R为根节点的子树是否包含了和树B一样的结构，采用递归实现。'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 and pRoot2:  # 两树均非空的时候，才进行比较。否则直接返回False
            if pRoot1.val == pRoot2.val:  # 如果找到了树A中对应树B的根节点，以这个根节点为起点判断是否包含树B
                result = self.DoesTree1hasTree2(pRoot1, pRoot2)
            if not result:  # 如果找不到，那么就再去树A中root的左儿子当作起点，去判断是否包含树B
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:  # 如果再找不到，那么就再去树A中root的右儿子当作起点，去判断是否包含树B
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result


    # 用于递归判断树的每个节点是否相同
    # 需要注意的地方是: 前两个if语句不可以颠倒顺序
    # 如果颠倒顺序, 会先判断pRoot1是否为None, 其实这个时候pRoot2的结点已经遍历完成确定相等了, 但是返回了False, 判断错误
    def DoesTree1hasTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True  # 如果树B已经遍历完了都能对应的上，返回true
        if pRoot1 == None:
            return False  # 如果树A先遍历完了，返回False
        if pRoot1.val != pRoot2.val:
            return False  # 如果其中有一个点没有对应上，返回False
        return self.DoesTree1hasTree2(pRoot1.left, pRoot2.left) and self.DoesTree1hasTree2(pRoot1.right, pRoot2.right)
        # 如果根节点对应的上，那么就分别去左右子节点里面匹配

