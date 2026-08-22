class Solution:
    def checkDivisibility(self, n: int) -> bool:
        li=list(map(int,str(n)))
        m=sum(li)
        a=1
        for i in range(len(li)):
            

            a=a*li[i]
        g=m+a
        if n%g==0:
            return True
        return False

        