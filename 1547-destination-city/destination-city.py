class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        c=0
        dici={}
        for i in range(len(paths)):
            if paths[i][0] not in dici:
                dici[paths[i][0]]=1
            else:
                dici[paths[i][0]]+=1 
            if paths[i][1] not in dici:
                dici[paths[i][1]] = 0       

        for j in dici:
            if dici[j]==0:
                return j

            
                
        