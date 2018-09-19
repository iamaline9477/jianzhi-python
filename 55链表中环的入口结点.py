#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

思路：
判断什么时候开始有环即可'''


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return None
        lst=[]
        while pHead:
            if pHead.next in lst:
                return pHead.next
            else:
                lst.append(pHead)
                pHead=pHead.next
        return None