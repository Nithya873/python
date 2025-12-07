class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l=[]
      
        for i in range(0,len(prices)):
            m=0
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    k=prices[i]-prices[j]
                    l.append(k)
                    m=1
                    break
                    
            if m==0:
                l.append(prices[i])                    

                    

                        
        
        return l        



        