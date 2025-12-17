class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        li1=s1.split() + s2.split()
        lii=[]
        for i in li1:
            if li1.count(i)==1:
                lii.append(i)
       
        return lii         

        
                   
              
                    
        