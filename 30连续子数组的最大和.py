#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:在古老的一维模式识别中,
常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

思路：
1、第一想法：
6,-3,-2,7,-15,1,2,2
-3,-2,7,-15,1,2,2
-2,7,-15,1,2,2
...
2
依次相加添加进list，求max
2、对于一个数A，若是A的左边累计数非负，那么加上A能使得值不小于A，认为累计值对整体和是有贡献的。
如果前几项累计值负数，则认为有害于总和，total记录当前和，maxsum记录最大和。'''

#way1
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return 0
        a = []
        newarray=array[:]
        while len(newarray)>= 1:
            for i in range(0, len(newarray)):
                a.append(newarray[i])
            newarray.pop()
            array.pop(0)
            newarray=[newarray[i] + array[i] for i in range(len(newarray))]
        return max(a)

#way2
# class Solution:
#     def FindGreatestSumOfSubArray(self, array):
#         if not array:
#             return 0
#         if len(array)==1:
#             return array[0]
#         total=array[0]
#         maxsum=array[0]
#         for i in array[1:]:
#             if total>=0:
#                 total+=i
#             else:
#                 total=i
#             if total>maxsum:
#                 maxsum=total
#         return maxsum