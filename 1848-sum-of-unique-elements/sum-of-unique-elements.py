class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dici={}
        for i in range(len(nums)):
            if nums[i] not in dici:
                dici[nums[i]]=1
            else:
                dici[nums[i]]+=1
        li=[]
        for j in dici:
            freq=dici[j]  
          
            if freq==1: 
                li.append(j)
        return sum(li)    

        