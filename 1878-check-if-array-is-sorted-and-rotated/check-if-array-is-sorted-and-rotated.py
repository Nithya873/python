class Solution:
    def check(self, nums: List[int]) -> bool:
        k=sorted(nums)
        c=0
        for i in range(len(nums)):
            if k==nums[i:]+nums[:i]:
                return True
        return False        
                     

        