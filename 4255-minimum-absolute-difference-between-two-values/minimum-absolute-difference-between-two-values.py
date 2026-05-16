class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        k=[]
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]==1 and nums[j]==2) or (nums[i]==2 and nums[j]==1):
                    ans=abs(i-j)
                    k.append(ans)
                    
        if len(k)==0:
            return -1
                    
        return min(k)   
                  


