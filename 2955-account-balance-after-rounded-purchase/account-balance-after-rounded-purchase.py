class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        l=purchaseAmount%10
       
        s=(10-l)
        k=purchaseAmount+s
        if l<5:
            k=purchaseAmount-l
          
        else:
            k=purchaseAmount+s
        return(100-k)    
        
    
        
           
        