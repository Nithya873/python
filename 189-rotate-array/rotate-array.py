class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        li=[]
        
        g=0
        k=k%len(nums)
    
        for i in range(len(nums)-1,-1,-1):
            if g<k:
                li.append(nums[i])
                g+=1
          
        
        for j in range(k):
            
            nums.pop()
        li.reverse()    


                
        nums[:]=li+nums
            
                 




        