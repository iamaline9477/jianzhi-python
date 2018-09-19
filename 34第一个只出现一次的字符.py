#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

思路：
1、count
2、用字典记录次数
3、建立哈希表'''

class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        return s.index(list(filter(lambda x:s.count(x)==1,s))[0])

# way2:
# class Solution:
#     def FirstNotRepeatingChar(self, s):
#         if not s:
#             return -1
#         dic = dict(zip(s, [0] * len(s)))
#         for letter in s:
#             dic[letter] += 1
#         for letter in s: #python3可改为for letter in dic
#             if dic[letter] == 1:
#                 return s.index(letter)
#                 break

# way3:
# class Solution:
#     def FirstNotRepeatingChar(self, s):
#         if not s:
#             return -1
#         ls=[0]*255 #8位ASCII范围为0~255
#         for i in s:
#             ls[ord(i)]+=1 #遍历字符串,下标为ASCII值,值为次数
#         for j in s:
#             if ls[ord(j)]==1:
#                 return s.index(j)
#                 break