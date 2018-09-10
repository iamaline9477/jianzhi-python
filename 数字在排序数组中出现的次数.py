#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
统计一个数字在排序数组中出现的次数。

思路：
排序数组 遍历 大于该数时不可能再出现 break'''

class Solution:
    def GetNumberOfK(self, data, k):
        count=0
        for i in range(len(data)):
            if data[i]==k:
                count+=1
            if data[i]>k:
                break
        return count

# way2:
# class Solution:
#     def GetNumberOfK(self, data, k):
#         return data.count(k)