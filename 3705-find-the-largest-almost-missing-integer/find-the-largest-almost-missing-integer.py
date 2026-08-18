class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        li=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                s=[]
                for u in range(i,j+1):
                    s.append(nums[u])
                if len(s)==k:

                    li.append(s)
        dici={}
        for w in li:
            for x in set(w):
                if x in dici:
                    dici[x]+=1
                else:
                    dici[x]=1
        m=-1
        for key,val in dici.items():
            if val==1:
                if m<key:
                    m=key
        return m
                
        



        