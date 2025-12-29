class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        
        c=0
       
        for i in range(len(words)):
            
            
            val=True
            
            for k in words[i]:
                if k not in allowed:
                    val=False
                    break
            if val:            
                c+=1    
        return c
       