class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zc=0
        mz=0
        co=0
        mco=0
        x=list(s)
        for i in x:
            if i=='0':
                zc+=1
                co=0
                
            mz=max(zc,mz)
            
            if i=='1':
                co+=1
                zc=0
            mco=max(co,mco)
            
        if mco>mz:
            return True
        else:
                 
            return False        
        