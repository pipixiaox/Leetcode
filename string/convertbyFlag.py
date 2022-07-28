# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 09:23:54 2022
@author: xiao.chen
From Leetcode 6
Type: ++
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        
        # 初始化结果列表，共numRows个，均为字符串
        resultList = ["" for _ in range(numRows)]
        
        # i= 0,1,2,...,numRows; flag = -1,1
        i, flag = 0, -1
        for c in s:
            resultList[i] += c
            
            # 当在首行和末行时反转flag
            if i ==0 or i == numRows-1:
                flag = -flag
            # flag=1, i: 0->numRows
            # flag=-1, i: numRows->0
            i += flag
        
        return "".join(resultList) # .join 将列表转换为字符串


if __name__ == "__main__":
    
    so = Solution()
    
    s = "abcdefghijklmnopqrstuvwxyz"
    numRows = 5
    
    result = so.convert(s, numRows)
    print(result)