#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

思路：
用lst删除重复结点，再重建链表'''

class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:
            return None
        lst1=[]
        while pHead:
            lst1.append(pHead.val)
            pHead=pHead.next
        lst1=list(filter(lambda x:lst1.count(x)==1,lst1))
        if not lst1:
            return None
        begin=ListNode(None)
        temp=ListNode(None)
        for i in lst1:
            if temp.val==None:
                temp.val=i
                begin=temp
            else:
                temp.next=ListNode(i)
                temp=temp.next
        return begin
