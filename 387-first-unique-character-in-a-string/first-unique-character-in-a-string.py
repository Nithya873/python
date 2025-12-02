class Solution:
    def firstUniqChar(self, s: str) -> int:
        dici={}
        for i in s:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        for j in range(len(s)):
            if dici[s[j]]==1:
                return j
             
        return -1    

        