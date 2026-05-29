class Solution:
    def minElement(self, nums: List[int]) -> int:
        li=[]
        
        for i in range(len(nums)):
            h=list(map(int,str(nums[i])))
            j=sum(h)

            li.append(j)
           
      
        return min(li)

              

        