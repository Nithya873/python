class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        k=list(s)
        li=[""]*len(s)
        for i in range(len(k)):
            pos=indices[i]
            li[pos]=s[i] 
        return "".join(li)     



         
                





        