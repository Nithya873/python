class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        k=len(nums)-1
        for i in range(0,len(nums)):
        
                if sum(nums[:i])==sum(nums[i+1:]):
                    return i
        return -1        
                
        
        