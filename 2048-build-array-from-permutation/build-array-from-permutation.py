class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums)):
            k=nums[nums[i]]
            li.append(k)

        return li    
