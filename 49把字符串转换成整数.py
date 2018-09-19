#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。
数值为0或者字符串不是一个合法的数值则返回0。

思路：
从高位向低位判断，再通过sum=sum*10+i更新'''


class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        symbol = 1
        if s[0] == '+':
            symbol = 1
            s = s[1:]
        elif s[0] == '-':
            symbol = -1
            s = s[1:]
        num = 0
        for i in range(len(s)):
            if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                num = 0
                break
            else:
                num = num * 10 + ord(s[i]) - ord('0')
        return symbol * num



