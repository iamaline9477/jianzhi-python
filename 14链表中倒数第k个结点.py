#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一个链表，输出该链表中倒数第k个结点。

思路：
注意k可能是0、可能是负数、可能大于链表长度的情况
另外返回的是结点，并不是结点的值'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    class Solution:
        def FindKthToTail(self, head, k):
            lst = []
            while head:
                lst.append(head)
                head = head.next
            if k <= 0 or k > len(lst):
                return None
            return lst[-k]