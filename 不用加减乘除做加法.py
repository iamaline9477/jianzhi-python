#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

思路：
位运算
用异或和移位操作，异或去不相同位，与取相同位，再左移，循环到进位为0即可。需要添加溢出判断。'''

class Solution:
    def Add(self, num1, num2):
        while num2:
            temp = (num1 ^ num2)& 0xffffffff
            num2 = ((num1 & num2) << 1)& 0xffffffff
            num1 = temp & 0xffffffff
        return num1 if num1<=0x7FFFFFF else ~(num1^0xffffffff)