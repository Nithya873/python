class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sici={}
        tici={}
        for i in s:
            if i not in sici:
                sici[i]=1
            else:
                sici[i]+=1
        for j in t:        
            if j not in tici:
                tici[j]=1
            else:
                tici[j]+=1
        for k in tici:
            if k not in sici or tici[k]>sici[k]:
                return k       