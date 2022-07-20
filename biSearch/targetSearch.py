# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:05:49 2022

@author: xiao.chen
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[left]:
                result = self.bisearch(nums,left,mid,target)
                left = mid
            else:
                result = self.bisearch(nums,mid,right,target)
                right = mid
            if result != -1:
                return result
        return -1
    
    def bisearch(self,nums:list[int],l:int,r:int,target:int) -> int:
        if nums[r-1] < target:
            return -1
        else:
            while l < r:
                m = (l+r)//2
                if nums[m] < target:
                    l = m+1
                elif nums[m] > target:
                    r = m
                else:
                    return m
            return -1
                
                
        


if __name__ == '__main__':
    s = Solution()
    nums = [6,8,9,10,15,17,1,2,4]
    target = 5
    result = s.search(nums, target)
    print(result)

