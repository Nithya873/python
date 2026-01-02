class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        k=len(nums)
        dici={}
        for i in nums:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1 
        for l in dici:
            if 2*dici[l]==k:
                return l        
         


        