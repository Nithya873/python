class Solution:
    def frequencySort(self, s: str) -> str:
        dici={}
        k=list(s)
        for i in range(len(k)):
            if k[i] not in dici:
                dici[k[i]]=1
            elif k[i] in dici:
                dici[k[i]]+=1
        p=[] 
        mixi=max(dici.values())
        for m in range(mixi,0,-1):
            for l in dici:
                if dici[l]==m:
                    p.append(l*m)
        return "".join(p)          


             

               

        