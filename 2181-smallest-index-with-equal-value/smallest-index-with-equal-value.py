class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        li=[]
        
        

        for i in range(len(nums)):
            k=nums[i]==i%10
            
            if nums[i]==i%10:
                li.append(i)
                i+=1
        if li!=[]:
            return li[0]
        else:
            return -1
              
        