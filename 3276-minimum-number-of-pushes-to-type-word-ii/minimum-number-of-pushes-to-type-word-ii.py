class Solution:
    def minimumPushes(self, word: str) -> int:
        h=len(word)
        dici={}
        for i in range(len(word)):
            if word[i]  in dici:
                dici[word[i]]+=1
            else:
                dici[word[i]]=1
        li=list(dici.values())
        li.sort(reverse=True)
        
        i=sum(li[:8])
        j=sum(li[8:16])*2
        k=sum(li[16:24])*3
        m=sum(li[24:26])*4
        if len(li)<=8:
            return i
        elif len(li)<=16:

    
            return i+j
        elif len(li)<=24:
            return i+j+k
        else:
            return i+j+k+m





