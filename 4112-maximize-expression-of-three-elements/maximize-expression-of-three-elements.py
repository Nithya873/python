class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        k=sorted(nums)
        l=k[-1]
        m=k[-2]
        j=k[0]
        return (l+m-(j))
        