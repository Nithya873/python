class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count=0
        while n>0:
            re=n%2
            if re==1:
                count+=1
            n=n//2

        return count

        