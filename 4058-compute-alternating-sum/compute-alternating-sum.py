class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        e=[]
        o=[]
        for i in range(len(nums)):
            if i%2==0:
                e.append(nums[i])
            if i%2!=0:    
                o.append(nums[i]) 
        return sum(e)-sum(o)     

        