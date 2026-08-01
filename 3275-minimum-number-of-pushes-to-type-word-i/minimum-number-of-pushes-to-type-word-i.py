class Solution:
    def minimumPushes(self, word: str) -> int:
        h=len(word)
        k=h//8
        if h<=8:
            return h
        elif h<=16:
            return 8+(h-8)*2
        elif h<=24:
            return 8+16+(h-16)*3
        else:
            return 8+16+24+(h-24)*4
        
        

        


             
        