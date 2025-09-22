class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        

        dici = {}
        for i in nums:
            if i in dici:
                dici[i] += 1             
            else:
                dici[i] = 1             
        mf=max(dici.values())
        total=0
        for key, val in dici.items():    
            if val ==mf:
                total+=val
        return total  
            
        