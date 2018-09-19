#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

思路：
如果有右子树，则找右子树的最左节点
如果没右子树，则找其父节点的父节点的父节点...直到当前节点是其父节点的左节点
退到了根节点仍没找到，则返回None'''

class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            pNode=pNode.right
            while pNode.left:
                pNode=pNode.left
            return pNode
        while pNode.next:
            if pNode==(pNode.next).left:
                return pNode.next
            else:
                pNode=pNode.next
        return None