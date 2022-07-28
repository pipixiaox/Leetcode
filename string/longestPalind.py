# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 14:37:27 2022
@author: xiao.chen
From Leetcode 5
Type: ++
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        result = ""
        i = 0
        maxNum = 0
        while i < len(s):
            # 统计当前字符从i+1后出现的次数
            num = s.count(s[i],i+1)
            # 仅出现一次的字符，无需统计
            if num <1:
                i +=1
                continue
            # 次数>=1的字符，查找另一字符的位置
            j = 0
            lastIndex = len(s)
            while j <num:
                # 从i+1开始查找最后一次出现的相同字符的index
                index = s.rfind(s[i],i+1,lastIndex)
                # 子串为从i:index+1之间的字符串
                s1 = s[i:index+1]
                # 当前子串小于最大子串，退出循环
                if len(s1) < maxNum:
                    break
                # 检查当前子串是否为回文
                if s1 == s1[::-1]:
                    maxNum = len(s1)
                    result = s1

                    break # 当为回文字符串时，继续下一次循环
                j +=1 #若不是回文串，继续查找下一个相同的字符
                lastIndex = index
            i += 1
            if len(s)-i < maxNum:
                break
        
        # 当循环无结果时，返回第一个字符
        if result == "":
            result = s[0]
        return result

if __name__ == "__main__":
    so = Solution()
    
    # s = "abbacafffffffffffffa"
    s = "abc"

    result = so.longestPalindrome(s)
    print(result)
