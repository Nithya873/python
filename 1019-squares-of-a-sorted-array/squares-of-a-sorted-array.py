class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        li=[]

        for i in range(len(nums)):
            k=nums[i]*nums[i]
            li.append(k)
        return sorted(li)  
        
        