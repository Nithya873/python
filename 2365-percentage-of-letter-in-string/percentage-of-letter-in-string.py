class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        d=list(s)
        dici={}
        for i in s:
            if i not in dici:
                dici[i]=1
            elif i in dici:
                dici[i]+=1  
        if letter not in dici:
            return 0
        return (dici[letter]*100)//len(d)   
                       
      