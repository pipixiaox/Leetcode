# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 15:11:20 2022
@author: xiao.chen
From Leetcode 1005
Type: +
"""

class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort(key=abs, reverse = True)
        for i in range(len(nums)):
            if k >0 and nums[i] <0:
                nums[i] *= -1
                k -= 1
        if k >0:
            nums[-1] *= (-1) **k
        return sum(nums)


if __name__ == "__main__":
    so = Solution()
    
    nums = [-4,-2,-3,1,2,3]
    k = 4
    
    result = so.largestSumAfterKNegations(nums, k)
    print(result)


    
    
    
    