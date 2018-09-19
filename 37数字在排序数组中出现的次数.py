#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
统计一个数字在排序数组中出现的次数。

思路：
1、排序数组 遍历 大于该数时不可能再出现 break（需要判断数据升序or降序）
2、二分查找'''

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

# way3:
#     def GetNumberOfK(self, data, k):
#         if not data or not k:
#             return 0
#         begin=0
#         end=len(data)-1
#         while begin<=end:
#             mid=(begin+end)//2
#             if k>data[mid]:
#                 begin=mid+1
#             elif k<data[mid]:
#                 end=mid-1
#             else:
#                 break
#         if begin>end:
#             return 0
#         begin=mid
#         end=mid
#         while begin>=0 and data[begin]==k:
#             begin-=1
#         while end<len(data) and data[end]==k:
#             end+=1
#         return end-begin-1
