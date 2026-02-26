class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        target=0
        li=[]
        for i in range(len(nums)-1):
            if nums[i]==key:
                target=nums[i+1]
                li.append(target)
        dici={}        
        for j in range(len(li)):
            if li[j] not in dici:
                dici[li[j]]=1
            else:
                dici[li[j]]+=1
        
        m = dict(sorted(dici.items(), key=lambda x: x[1], reverse=True))
        li=[]
        for k in m:
            return k    

            


            
        