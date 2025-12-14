class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        m=sorted(nums)
        li=[]
        for i in range(len(m)):
            if m[i]==target:
                li.append(i)
        return li    
            
            


        

        