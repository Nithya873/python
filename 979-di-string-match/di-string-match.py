class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low=0
        high=len(s)
        li=[]

        for i in range(0,len(s)):
            if s[i]=='I':
                li.append(low)
                low+=1
            elif s[i]=='D':
                li.append(high)
                high-=1
        li.append(low)        
        return li        





        