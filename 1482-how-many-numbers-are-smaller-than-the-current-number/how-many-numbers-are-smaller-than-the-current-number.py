class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c=0
        li=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    c+=1
                    
            li.append(c)
                    
        return li           
        