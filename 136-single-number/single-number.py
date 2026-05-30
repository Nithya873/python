class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nici={}
        for i in range(len(nums)):
            if nums[i] in nici:
                nici[nums[i]]+=1
            else:
                nici[nums[i]]=1
        c=0        
        for key,vl in nici.items():
            if vl ==1:
                
                return key     

                     
        