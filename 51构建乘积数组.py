#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

思路：
1、按规则构建
2、三角数组'''

#way1
class Solution:
    def multiply(self, A):
        if not A:
            return []
        result=[]
        for  i in range(len(A)):
            res1=1
            for j in range(len(A)):
                if j!=i:
                    res1*=A[j]
                else:
                    j+=1
            result.append(res1)
        return result

#way2:
# def multiply(self, A):
#         head = [1]
#         tail = [1]
#         for i in range(len(A)-1):
#             head.append(A[i]*head[i])
#             tail.append(A[-i-1]*tail[i])
#         return [head[j]*tail[-j-1] for j in range(len(head))]