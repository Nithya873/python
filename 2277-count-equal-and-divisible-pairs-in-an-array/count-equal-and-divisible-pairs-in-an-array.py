class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l=i*j
                if nums[i]==nums[j] and l%k==0:
                    c+=1
        return c            
        