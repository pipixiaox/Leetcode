# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 15:11:20 2022
@author: xiao.chen
From Leetcode 1005
Type: +
"""

class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        if nums[0] >=0:
            if k % 2 ==0:
                return sum(nums)
            else:
                return sum(nums[1:])-nums[0]
        
        m = self.findMinusNum(nums)
        if m < k:
            if (k-m) % 2 == 0:
                return sum(nums[m:])-sum(nums[0:m])
            else:
                # if m == len(nums):
                #     return sum(nums[m-1:])-sum(nums[0:m-1])
                if m == len(nums) or abs(nums[m-1]) < abs(nums[m]):
                    return sum(nums[m-1:])-sum(nums[0:m-1])
                else:
                    return sum(nums[m+1:])-sum(nums[0:m+1])
        else:
            return sum(nums[k:])-sum(nums[0:k])
        
    def findMinusNum(self, nums):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right) //2
            if nums[mid] >=0 and nums[mid-1] <0:
                return mid
            elif nums[mid] <0:
                left = mid +1
                continue
            else:
                right = mid
                continue
        return left

if __name__ == "__main__":
    so = Solution()
    
    nums = [-4,-2,-3,1,2,3]
    k = 4
    
    result = so.largestSumAfterKNegations(nums, k)
    print(result)


    
    
    
    