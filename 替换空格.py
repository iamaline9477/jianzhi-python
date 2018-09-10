#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。

思路：
不利用函数怎么做？'''


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ','%20')

    # way2:
    # def replaceSpace(self, s):
    #     # write code here
    #     s1=''
    #     for a in s:
    #         if a.isspace():
    #             s1+='%20'
    #         else:
    #             s1+=a
    #     return s1