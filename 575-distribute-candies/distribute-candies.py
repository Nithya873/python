class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        m=set(candyType)
        k=len(m)
        n=len(candyType)
        s=n//2
        if s<=k:
            return s
        elif k<s:
            return k   
        