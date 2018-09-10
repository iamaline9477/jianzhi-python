#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

思路：
可以直接用reverse
可以用栈（后进先出）
还可以倒序插入
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        a=[]
        while listNode:
            a.append(listNode.val)
            listNode = listNode.next
        a.reverse()
        return a
        #return a[::-1]
# way2:
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         a = []
#         while listNode:
#             a.insert(0, listNode.val)
#             listNode = listNode.next
#         return a
#
# way3:
# import collections
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         a=collections.deque()
#         while listNode:
#             a.appendleft(listNode.val)
#             listNode = listNode.next
#         return a