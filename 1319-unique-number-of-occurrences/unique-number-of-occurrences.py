class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dici={}
        for i in range(len(arr)):
            if arr[i] in dici:
                dici[arr[i]]+=1
            else:
                dici[arr[i]]=1
        flag=0        
        m=list(dici.values())
        k=sorted(m)
        
        for j in range(len(k)-1):
            

            if k[j]==k[j+1]:
                flag+=1
        if flag>0:
            return False
        
        return True    


            

            

        