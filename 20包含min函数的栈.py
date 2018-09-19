#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
定义栈的数据结构，
请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

思路：
每入栈一次，就与辅助栈顶比较大小，如果小就入栈，如果大就入栈当前的辅助栈顶
当出栈时，辅助栈也要出栈'''

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []  # 辅助栈

    def push(self, node):
        min = self.min()
        if not min or node < min:
            self.stack2.append(node)
        else:
            self.stack2.append(min)
        self.stack1.append(node)

    def pop(self):
        if self.stack1:
            self.stack2.pop()
            return self.stack1.pop()

    def top(self):
        if self.stack1:
            return self.stack1[-1]

    def min(self):
        if self.stack2:
            return self.stack2[-1]