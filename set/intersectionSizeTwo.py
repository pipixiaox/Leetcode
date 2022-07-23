# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 16:24:23 2022
@author: xiao.chen
from Leetcode 757. 设置交集大小至少为2
难度：困难
"""

class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        if len(intervals) ==1:
            return 2
        
        # 对列表进行排序，区间从小到大
        intervals.sort(key= lambda x: (x[0],x[1]))

        # 初始化setR
        setR = {x for x in range(intervals[0][0],intervals[0][1]+1)}
        if len(setR) >= 2:
            r = 2 # 初始化结果
        
        flag = False
        
        # 遍历列表区间，根据首尾值形成 set 集合
        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            set1 = {x for x in range(start,end+1)}
            
            # 计算交集
            nsetR = set1 & setR

            if len(nsetR) >=2:
                setR = nsetR
                if flag:
                    r +=1
                    flag = False
            elif len(nsetR) ==1:
                flag = True
                setR = {x for x in range(start+1,end+1)}
                r +=1
            else:
                setR = set1
                r +=2
                flag = False
        return r

if __name__ == '__main__':
    so = Solution()
    intervals = [[1,3],[3,7],[5,7],[7,8]]
    # intervals = [[1,3],[1,4],[2,5],[3,5]]
    result = so.intersectionSizeTwo(intervals)
    print(result)