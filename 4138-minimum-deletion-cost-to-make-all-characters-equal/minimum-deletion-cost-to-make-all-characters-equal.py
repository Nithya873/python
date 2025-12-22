class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        total=sum(cost)
        dici={}
        for i in range(len(s)):
            if s[i] in dici:
                dici[s[i]]+=cost[i]
            else:
                dici[s[i]]=cost[i]
        ans=float('inf')   
        for j in dici:
            ans=min(ans,total-dici[j])         
        return ans 
            
            
                 
     
        