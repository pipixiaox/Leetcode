# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 16:02:25 2022
@author: xiao.chen
from Leetcode 409. 最长回文串
难度：简单
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <=1:
            return len(s)
        
        exited = []
        sumNum = 0
        # 奇数个数标志位，当存在奇数个数时为真
        flag = False
        for i in range(len(s)):
            if s[i] in exited:
                continue
            else:
                num = s.count(s[i])
                if num % 2 == 0: 
                    sumNum += num
                else:
                    flag = True # 一旦存在奇数个数，则flag保持为True
                    sumNum += num-1
                exited.append(s[i])
        if flag:
            return sumNum+1
        else:
            return sumNum


if __name__ == '__main__':
    so = Solution()
    s= "bbccef"
    result = so.longestPalindrome(s)
    print(result)