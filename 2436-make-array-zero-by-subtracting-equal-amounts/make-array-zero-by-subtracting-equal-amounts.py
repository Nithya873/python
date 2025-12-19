class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        c=0
        while sum(nums)!=0:
            k=min(i for i in nums if i!=0)
            li=[]
        
            for i in nums:
                if i!=0:

            
                    li.append(i-k)
                else:
                    li.append(i)    
            
            nums=li 
            c+=1   
        return c 

   

        