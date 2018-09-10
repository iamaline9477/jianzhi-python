#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一个链表，反转链表后，输出新链表的表头。

思路：
tmp记录下一个要反转的结点，pre指向反转后的首结点，pHead始终指向要反转的结点
每反转一个结点，把pHead结点的下一个结点指向pre，pre指向反转后首结点, 再把pHead移动到下一个要反转的结点(=tmp)。直至None结束
需要考虑链表只有0 or 1个元素的情况。'''

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.val:
            return None
        pre=None
        while pHead:
            tmp=pHead.next
            pHead.next=pre
            pre=pHead
            pHead=tmp
        return pre