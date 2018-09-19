#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

思路：
数字转为str
if a+b>b+a b应在a的前面
最后拼接转数字输出'''

class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        s = list(map(str, numbers))
        for i in range(0, len(s)):
            for j in range(i + 1, len(s)):
                if s[i] + s[j] > s[j] + s[i]:
                    s[i], s[j] = s[j], s[i]#注意调换同一list中元素不可分行写
        return ''.join(s).lstrip('0') or'0' #注意[0,0,0,1]或[0,0,0,0]情形 需要去除左边多余的0

#其中循环排序的4句可改为：
#numbers.sort(cmp=lambda x,y:cmp(x+y,y+x)) python2写法
