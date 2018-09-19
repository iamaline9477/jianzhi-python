#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

'''题目描述：
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

思路：
位运算
用异或和移位操作，异或取不相同位，与取相同位，再左移，循环到进位为0即可。需要添加溢出判断。
如5-101，7-111的相加过程：
第一步：相加各位的值，不算进位，得到010，二进制每位相加就相当于各位做异或操作，101^111=010。
第二步：计算进位值，得到1010，相当于各位做与操作得到101，再向左移一位，(101&111)<<1=1010。
第三步：重复上述两步，每位相加010^1010=1000，进位值(010&1010)<<1=100。
第四步：继续重复上述两步：1000^100 = 1100，但进位值(1000&100)<<1=0，故跳出循环，1100为最终结果。'''

class Solution:
    def Add(self, num1, num2):
        while num2:
            temp = (num1 ^ num2)& 0xffffffff
            num2 = ((num1 & num2) << 1)& 0xffffffff #进位
            num1 = temp & 0xffffffff
        return num1 if num1<=0x7FFFFFF else ~(num1^0xffffffff) #对负数的处理