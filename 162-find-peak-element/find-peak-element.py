class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        h=max(nums)
        for i in range(len(nums)):
            if nums[i]==h:
                return i
        