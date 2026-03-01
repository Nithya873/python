class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        l=0
        dici={}
        ans=0
        for i in range(len(s)):
            if s[i] not in dici:
                dici[s[i]]=1
            else:
                dici[s[i]]+=1
            if i-l==3:
                dici[s[l]]-=1
                if dici[s[l]]==0:
                    dici.pop(s[l])
                l+=1
            if len(dici)==3:
                ans+=1   
        return ans          

              
        
      

                    


        
              


