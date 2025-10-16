class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        r=[]
        e=[]
        o=[]
        for j in nums:
            if j%2==0:
                e.append(j)
            else:
                o.append(j)    

    
        for i in range(len(nums)):
        

            if i%2==0:
                r.append(e.pop())
            else:
                r.append(o.pop())
        return r            
        