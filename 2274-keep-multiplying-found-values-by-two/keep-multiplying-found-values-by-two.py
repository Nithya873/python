class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        k=original
        for i in nums:
            if k in nums:
                k=k*2
        return k        


        