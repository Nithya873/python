class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        h=sorted(nums)
        li=[]
        
        for i in range(len(h)):
            li.append(h[-1]-1)
            li.append(h[-2]-1)
            break
        
        k=math.prod(li)
        return k


        





        