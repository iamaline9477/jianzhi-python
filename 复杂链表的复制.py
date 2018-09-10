#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一个复杂链表（每个节点中有节点值，以及两个指针，
一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

思路：
1. 把复制的结点链接在原始链表的每一对应结点后面
2. 把复制的结点的random指针指向被复制结点的random指针的下一个结点
3. 拆分成两个链表，奇数位置为原链表，偶数位置为复制链表，
注意复制链表的最后一个结点的next指针不能跟原链表指向同一个空结点None，
next指针要重新赋值None(判定程序会认定你没有完成复制）'''



# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        pCur = pHead
        while pCur:
            pCur_next = pCur.next
            copynode = RandomListNode(pCur.label)
            copynode.next = pCur_next
            pCur.next = copynode
            pCur = pCur_next

        pCur = pHead
        while pCur:
            pCur_random = pCur.random
            copynode = PCur.next
            if pCur_random:
                copynode.random = pCur_random.next
            pCur = copynode.next

        pCur = pHead
        copyHead = pHead.next
        while pCur:
            copynode = pCur.next
            pCur_next = copynode.next
            pCur.next = pCur_next
            if pCur_next:
                copynode.next = pCur_next.next
            else:
                copynode.next = None
            pCur = pCur_next
        return copyHead
