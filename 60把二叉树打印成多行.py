#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

思路：
层次遍历
注意换层'''

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        currentlevel=[pRoot]
        nextlevel=[]
        result=[]
        while currentlevel:
            res=[]
            for node in currentlevel:
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
                res.append(node.val)
            result.append(res)
            currentlevel=nextlevel
            nextlevel=[]
        return result