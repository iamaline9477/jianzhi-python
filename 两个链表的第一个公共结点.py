#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入两个链表，找出它们的第一个公共结点。

思路：
1、依次将链表中的元素压入两个栈中，然后每次从两个栈中抛出一个元素，直到抛出的结点相同时返回
后面的元素都是公共的
2、让长的那个链表先走完长的长度，再比较后面的结点（因为从相同的结点开始后面都是相同的）'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        stack1 = []
        stack2 = []
        result = []
        if not pHead1 or not pHead2:
            return None
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1 == node2:
                result.append(node1)
        if result: #不能直接输出是因为result是一个list
            node = result.pop()
            return node

# way2:
# class Solution:
#     def FindFirstCommonNode(self, pHead1, pHead2):
#         len1 = self.length(pHead1)
#         len2 = self.length(pHead2)
#         if len1 > len2:
#             len_diff = len1 - len2
#             while len_diff:
#                 pHead1 = pHead1.next
#                 len_diff -= 1
#         elif len2 > len1:
#             len_diff = len2 - len1
#             while len_diff:
#                 pHead2 = pHead2.next
#                 len_diff -= 1
#         while pHead1 and pHead2:
#             if pHead1 == pHead2:
#                 return pHead1
#             else:
#                 pHead1 = pHead1.next
#                 pHead2 = pHead2.next
#         return None
#
#     def length(self, pHead):
#         if not pHead:
#             return 0
#         l = 0
#         while pHead:
#             l += 1
#             pHead = pHead.next
#         return l



