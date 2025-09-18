class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort(reverse=False)
        a=max(nums)
        b=min(nums)
        
        for i in nums:
            if len(nums)>=3:
                nums.remove(a) and nums.remove(b)
                return nums[1]
            else:
                return -1
            
           


        