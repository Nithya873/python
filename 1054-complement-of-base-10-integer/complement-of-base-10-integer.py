class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=bin(n)[2:]
        li=[int(i) for i in s]
        li2=[]
        for j in range(len(li)):
            if li[j]==0:
                li2.append(1)
            else:
                li2.append(0)  
        k="".join(str(h) for h in li2)  
        f=(int(k,2))
        return f      

 

        