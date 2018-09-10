#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
如果不存在则输出0。

思路：
1、用字典设置计数，超过一半则返回
2、采用阵地攻守的思想：
第一个数字作为第一个士兵，守阵地；count = 1；
遇到相同元素，count++;
遇到不相同元素，即为敌人，同归于尽,count--；当遇到count为0的情况，又以新的i值作为守阵地的士兵，继续下去，到最后还留在阵地上的士兵，有可能是主元素。
再加一次循环，记录这个士兵的个数看是否大于数组一半即可。'''

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if numbers==[]:
            return 0
        s=dict(zip(numbers,[0]*len(numbers)))
        for num in numbers:
            s[num]+=1
        if s[key]>(len(numbers)/2.0):
                return key
        return 0

# way2:
# class Solution:
#     def MoreThanHalfNum_Solution(self, numbers):
#         if numbers==[]:
#             return 0
#         val,count=None,0
#         for num in numbers:
#             if count==0:
#                 val=num
#                 count=1
#             if num==val:
#                 count+=1
#             else:
#                 count-=1
#         if numbers.count(val)>len(numbers)/2.0:
#             return val
#         else:
#             return 0