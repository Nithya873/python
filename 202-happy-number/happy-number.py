class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            
            nums=list(map(int,str(n)))
            anss=0
            for i in range(len(nums)):
                anss=anss+nums[i]*nums[i]
            n=anss    
        
        return n==1    
            
        


       