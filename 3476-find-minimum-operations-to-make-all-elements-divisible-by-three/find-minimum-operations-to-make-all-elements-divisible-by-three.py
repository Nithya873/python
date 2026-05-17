class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a=0
        for i in range(len(nums)):
            if nums[i]%3!=0:
                a+=1
        return a        
        