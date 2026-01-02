class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        k=sorted(prices)
        li=[]
        for i in range(len(k)-1):
            m=k[i]+k[i+1]
            li.append(m)
            for j in range(len(li)):
                if li[j]<=money:
                    return money-li[j]
          
            
            return money
            
                

        return p    
           
        