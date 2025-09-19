
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)        # length
        s = set(nums)        # set of numbers
        for i in range(1, n+2):
            if i not in s:
                return i
        if n <= 1:
            return i+1
 



        