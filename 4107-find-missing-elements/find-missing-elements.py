class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        k=sorted(nums)
        li=[]
        
        for i in range(len(k)-1):
            c=k[i]+1
            

            while c<k[i+1]:
            
            
                li.append(c)
                c+=1
        
        return li


                
                
    
