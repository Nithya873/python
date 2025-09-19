class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dici={}
        for i in nums:
            if i in dici:
                return i
            else:
                dici[i]=1    
         

        