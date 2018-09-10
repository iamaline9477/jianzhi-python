#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。
请写程序找出这两个只出现一次的数字。

思路：
异或的性质：两个相同数字异或=0，一个数和0异或还是它本身。
从头到尾依次异或数组中的每一个数字，最终得到的结果就是两个只出现一次的数字的异或结果。
由于这两个数字肯定不一样，这个结果数字的二进制表示中至少有一位为1 。
在结果数字中找到第一个为1的位置，记为第N位。以第N 位是不是1为标准把原数组中的数字分成两个子数组，
再在子数据中异或得到两个结果。'''


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        tmp = 0
        idx = 0
        for num in array:
            tmp ^= num
        while (tmp & 1) == 0:
            tmp >>= 1
            idx += 1
        a = 0
        b = 0
        for num in array:
            if self.isBit(num, idx):
                a ^= num
            else:
                b ^= num
        return [a, b]

    def isBit(self, num, idx):
        num >>= idx
        return num & 1

# way2:
# -*- coding:utf-8 -*-
# class Solution:
#     # 返回[a,b] 其中ab是出现一次的两个数字
#     def FindNumsAppearOnce(self, array):
#         hashmap={}
#         for num in array:
#             if num in hashmap:
#                 hashmap[num]+=1
#             else:
#                 hashmap[num]=1
#         res=[]
#         for k in hashmap.keys():
#             if hashmap[k]==1:
#                 res.append(k)
#         return res

# way3:
# class Solution:
#     # 返回[a,b] 其中ab是出现一次的两个数字
#     def FindNumsAppearOnce(self, array):
#         if not array:
#             return []
#         return filter(lambda x:array.count(x)%2==1,array)

