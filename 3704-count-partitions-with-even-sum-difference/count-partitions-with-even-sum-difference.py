class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        l=len(nums)
        s=0
        for i in range(len(nums)):
            s=s+nums[i]
            i+=1
        if s%2==0:
            return l-1 
        else:
            return 0      
            





        