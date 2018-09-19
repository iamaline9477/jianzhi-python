#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

思路：
1、直接用reverse
2、逆序插入(可以考虑deque的appendleft
2、用栈（后进先出）
注意是返回链表值
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# way1:
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

#way3(多此一举hhh）
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         if not listNode:
#             return []
#         result = []
#         while listNode:
#             result.append(listNode.val)
#             listNode = listNode.next
#         result2 = []
#         while result:
#             result2.append(result.pop())
#         return result2
