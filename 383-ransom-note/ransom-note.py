class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rici={}
        mici={}
        for i in ransomNote:
            if i not in rici:
                rici[i]=1
            else:
                rici[i]+=1
        for j in magazine:
            if j not in mici:
                mici[j]=1
            else:
                mici[j]+=1
        for k in rici:
            if k not in mici or mici[k]<rici[k]:
                
                return False
        return True                                 

        