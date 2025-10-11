class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxs=nums[0]
        maxi=0
        for i in range(len(nums)):
            if nums[i]>maxs:
                maxs=nums[i]
                maxi=i
        for i in range(len(nums)):
            
            if i!=maxi and maxs<2*nums[i]:

                return -1   
        return maxi             

         
        