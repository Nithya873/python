class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dici={}
        paragraph=paragraph.lower()
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        word=paragraph.split()
        for i in range(len(word)):
            if word[i]  in dici:
                dici[word[i]]+=1
            else:
                dici[word[i]]=1
        for k in banned:
            if k in dici:
                del dici[k]  
        li=max(dici,key=dici.get) 
        return li            
      

                    
        
            


        