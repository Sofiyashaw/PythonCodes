# -*- coding: utf-8 -*-
"""
Created on Sun May 19 23:10:51 2024

@author: jacin
"""

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)<=2:
          return len(nums)

        i=2
        for j in range(2,len(nums)):
            if nums[j]!=nums[i-2]:
                nums[i]=nums[j]  
                i+=1
        return i
sol=Solution()
nums = [1,1,1,2,2,3]
sol.removeDuplicates(nums)               

