#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。

思路：
首先判断两个表头是否为空，若其中一个为空，返回不为空的那个表头（均为空的情形也被包括在内）
else 比较两个表头关键值的大小，返回具有较小关键值的表头ret，ret指向下一个递归求得的元素'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            ret = pHead1
            ret.next = self.Merge(pHead1.next, pHead2)
        else:
            ret = pHead2
            ret.next = self.Merge(pHead1, pHead2.next)
        return ret
