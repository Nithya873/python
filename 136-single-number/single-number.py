class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dici={}
        for i in range(len(nums)):
            if nums[i] not in dici:
                dici[nums[i]]=1
            else:
                dici[nums[i]]+=1
        for key,value in dici.items():
            if value==1:
                return key
          

                     
        