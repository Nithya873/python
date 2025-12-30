class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        h=[]
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    h.append((min(nums[i],nums[j]),max(nums[i],nums[j])))
        k=set(h)            
        return len(k)            
        