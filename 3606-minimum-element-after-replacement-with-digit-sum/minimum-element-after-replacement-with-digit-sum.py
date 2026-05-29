class Solution:
    def minElement(self, nums: List[int]) -> int:
        li=[]
        k=sorted(nums)
        for i in range(len(nums)):
            h=list(map(int,str(k[i])))
            j=sum(h)

            li.append(j)
        g=sorted(li)    
      
        return g[0]

              

        