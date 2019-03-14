#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# Author: SONG

# 题目描述：
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

# 思路一：
#  - 新建字符串，依次遍历输入字符串，若为空格则替换后加入新字符串，若非空格则直接加入。
# 运行时间：22ms
# 占用内存：5860k
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        l=''
        for i in s:
            if i==' ':
                l+='%20'
            else:
                l+=i
        return l

		
# 思路二：
#  - 用split函数根据空格对字符串进行划分，转为list，再用join函数连接成字符串。
# 运行时间：20ms
# 占用内存：5728k
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return '%20'.join(s.split(' '))
		
		
# 思路三：
#  - 调用python中字符串替换函数。
#运行时间：28ms
#占用内存：5752k
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return s.replace(' ','%20')
		

# 思路四：
#  - 从前往后遍历字符串，记录空格个数，得到替换后应有的字符串长度；
#  - 从后往前遍历替换后字符串长度，若遇空格则通过修改下标依次加入'%','2’,'0'，否则加入原字符串中元素。
# 注意：由于python中不能直接修改字符串，上述方法需要进行间接修改。
#运行时间：23ms
#占用内存：5736k
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        l=len(s)
        blank=0
        for i in range(l):
            if s[i]==' ':
                blank+=1
        res=[0]*(l+2*blank)#借助一个list来修改字符串
        for i in range(l-1,-1,-1):
            if s[i]!=' ':
                res[i+2*blank]=s[i]
            else:
                res[i+2*blank]='0'
                res[i+2*blank-1]='2'
                res[i+2*blank-2]='%'
                blank-=1
        return ''.join(res)