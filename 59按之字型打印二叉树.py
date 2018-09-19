#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

思路：
层次遍历的变型，用count标志打印方向'''

class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        queue=[pRoot]
        count=0
        result=[]
        next_queue=[]
        while queue:
            res=[]
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                res.append(node.val)
            queue=next_queue
            next_queue=[]
            if count%2==0:
                result.append(res)
            else:
                result.append(res[::-1])
            count+=1
        return result