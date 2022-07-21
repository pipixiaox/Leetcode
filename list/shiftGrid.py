# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 20:40:30 2022
@author: xiao.chen
from Leetcode 1260.二维网格的迁移
难度：简单
"""


from collections import deque
class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:

        # m行n列
        m = len(grid)
        n = len(grid[0])
        
        # 二维列表转一维
        ngrid = []
        for g in grid:
            ngrid.extend(g)
        
        # 一维列表转队列，并进行旋转
        # k>0时将队列右侧k位元素添加到队列左侧
        dq = deque(ngrid)
        dq.rotate(k)
        nngrid = list(dq)
        # print(nngrid)
        # nngrid = list(deque(ngrid).rotate(k)) ??
        

        # 一维列表转二维
        # if n == 1:
        #     result = [[nngrid[i]] for i in range(m)]
        
        # else:
        #     result = []
        #     for i in range(m):
        #         result.append(nngrid[i*n:n*(i+1)])
        
        # 直接利用列表表达式将一维列表转二维
        result = [nngrid[n*i:n*(i+1)] for i in range(m)]
        
        return result


if __name__ == '__main__':
    s = Solution()
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    result = s.shiftGrid(grid, k)
    print(result)