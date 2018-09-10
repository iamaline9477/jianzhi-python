#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入两个整数序列，第一个序列表示栈的压入顺序，
请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）

思路：
用一个辅助栈压入入栈元素
若栈顶元素等于出栈序列头则出辅助栈
出栈序列头转向下一个元素
最后判断辅助栈是否为空'''


class Solution:
    def IsPopOrder(self, pushV, popV):
        if not popV:
            return False
        a=[]
        a.append(pushV.pop(0))
        while a:
            if a[-1]==popV[0]:
                a.pop()
                popV.pop(0)
            elif pushV:
                a.append(pushV.pop(0))
            else:
                return False
        return True