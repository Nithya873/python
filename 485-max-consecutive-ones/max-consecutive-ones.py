class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones=0
        max_ones=0
        for i in nums:
            if i==1:
                ones=ones+1
                
            else :
    
                max_ones=max(ones,max_ones)
                ones=0
        return max(max_ones,ones)          

        