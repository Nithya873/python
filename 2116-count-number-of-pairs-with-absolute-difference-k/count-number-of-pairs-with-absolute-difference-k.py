class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            
            for j in range(len(nums)-1,0,-1):
                if abs(nums[i]-nums[j])==k and i<j:
                    c+=1
        return c            
        