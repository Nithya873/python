class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        j=len(nums)
        l=0
        temp=0
        ans=float("inf")
        for i in range(len(nums)):
            temp+=nums[i]
            if i-l==k:
                temp-=nums[l]
                l+=1
            if i-l+1==k:
                ans=min(ans,nums[i]-nums[l])    
        return ans        

        
        
       
        