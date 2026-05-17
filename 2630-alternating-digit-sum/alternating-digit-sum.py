class Solution:
    def alternateDigitSum(self, n: int) -> int:
        e=[]
        o=[]
        m=list(map(int,str(n)))
        for i in range(len(m)):
            if i%2==0:
                e.append(m[i])
            if i%2!=0:
                o.append(m[i])  
        return sum(e)-sum(o)          
       