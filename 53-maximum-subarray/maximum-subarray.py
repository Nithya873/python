class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=-inf
        h=0
        for i in range(len(nums)):
           h+=nums[i]
           if h>m:
            m=h
           if h<0:
            h=0
            

        return m
      
        