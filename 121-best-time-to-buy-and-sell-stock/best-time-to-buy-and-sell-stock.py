class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        mp=0
        for i in range(len(prices)):
            cost=prices[i]-mini
            mp=max(mp,cost)
            mini=min(mini,prices[i])
        return mp
        
            
        