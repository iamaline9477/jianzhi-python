#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。

思路：
构建[0]*256的list，记录出现记录，输出每一次只出现一次的字符'''


class Solution:
    def __init__(self):
        self.stack = [0] * 256
        self.s = ''

    def FirstAppearingOnce(self):
        for i in range(len(self.s)):
            if self.stack[ord(self.s[i])] == 1:
                return self.s[i]
        else:
            return '#'

    def Insert(self, char):
        self.s += char
        self.stack[ord(char)] += 1