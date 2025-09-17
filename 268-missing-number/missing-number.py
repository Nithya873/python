class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        k=len(nums)
        l=k*(k+1)//2
        m=l-sum(nums)
        return m    

        