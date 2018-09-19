#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串
abc,acb,bac,bca,cab和cba。

思路：
固定第一个字符，递归取得首位后面的各种字符串组合
注意要按字典排序'''

class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        if len(ss)==1:
            return [ss]
        a=[]
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                if ss[i]+j not in a:#避免重复
                    a.append(ss[i]+j)
        return sorted(a) #调整顺序