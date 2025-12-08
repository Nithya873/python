class Solution:
    def defangIPaddr(self, address: str) -> str:
        l=list(address)
        k=[]
        for i in address:
            if i=='.':
                i='[.]'
                k.append(i)
            else:
                k.append(i)    
        return ''.join(k)        
        