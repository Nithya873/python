class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dici={}
        for i in range(len(nums)):
            if nums[i] not in dici:
                dici[nums[i]]=1
            else:
                dici[nums[i]]+=1 
        ans=[]
        temp=len(nums)//3
        for i in dici:
            val=dici[i] 
            if val>temp:
                ans.append(i)
        
        return ans                 
        