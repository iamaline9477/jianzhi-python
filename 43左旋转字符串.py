#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
汇编语言中有一种移位指令叫做循环左移（ROL），
现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。

思路：
1、复制一个字符串，顺次取
2、切片
3、S=XY，YX=(X^T*Y^T)^T'''

class Solution:
    def LeftRotateString(self, s, n):
        l = len(s)
        if len(s) == 0:
            return ''
        s = s + s
        n = n % l
        return s[n:n + l]

# way2:
# class Solution:
#     def LeftRotateString(self, s, n):
#         if not s:
#             return ''
#         n=n%len(s)
#         return s[n:]+s[0:n]

# way3:
# class Solution:
#     def LeftRotateString(self, s, n):
#         if not s:
#             return ''
#         n = n % len(s)
#         s = self.MyReverse(s, 0, n - 1)
#         s = self.MyReverse(s, n, len(s) - 1)
#         s = self.MyReverse(s, 0, len(s) - 1)
#         return s
#
#     def MyReverse(self, s, start, end):
#         if not s:
#             return ''
#         a = list(s)
#         while start < end:
#             temp = a[start]
#             a[start] = a[end]
#             a[end] = temp
#             start += 1
#             end -= 1
#         return ''.join(a)