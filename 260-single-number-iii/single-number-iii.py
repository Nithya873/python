class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c={}
        for i in nums:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        result=[]        
        for i,count in c.items():
            if count==1:
                result.append(i)
        return result        

                            
        