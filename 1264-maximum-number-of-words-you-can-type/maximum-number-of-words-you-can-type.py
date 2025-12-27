class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l=text.split()
        m=set(brokenLetters)
        
        c=0
        for i in l:
            for j in m:
                if j in i:
                    break
            else:
                c+=1        
            
       
                    
        return c  