# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:49:40 2022
@author: xiao.chen
From Leetcode 6
Type: ++
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1:
            return s
        resultDict = {}
        # 每个端点列两两字符间隔为2N-2
        for i in range(numRows):
            resultDict[i] = s[i::2*numRows-2]
        
        insertDict = {}

        # 将 中间行 非端点列 插入
        for j in range(1,numRows-1):
            r = []
            # 非端点列两两字符间隔也为2N-2
            insertDict[j] = s[2*numRows-2-j::2*numRows-2]
            # 将非端点列插入到端点列中
            for k in range(len(insertDict[j])):
                r.extend(resultDict[j][k] + insertDict[j][k])
            
            # 将列表转换为str，端点列可能比非端点列长度长
            if len(insertDict[j]) == len(resultDict[j]):
                resultDict[j] = "".join(r)
            else:
                resultDict[j] = "".join(r) + resultDict[j][-1]
        
        # 将字典转换为列表再转换为str输出
        r = []
        for i in range(numRows):
            r.extend(resultDict[i])
        
        result = "".join(r)
        return result
                
        




if __name__ == "__main__":
    so = Solution()
    
    s = "ABCDEFGHIJKLMNOPQRST"
    numRows = 5

    result = so.convert(s,numRows)
    print(result)
            