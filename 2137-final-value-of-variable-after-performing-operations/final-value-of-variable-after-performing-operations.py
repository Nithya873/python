class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        m=len(operations)
        
        t=0
        a=0
        
        for i in range(len(operations)):
            
            if operations[i]=='--X' or operations[i]=='X--':
                operations[i]=-1
                t=a+operations[i]
                a=t
            elif operations[i]=='X++'or operations[i]=='++X':
                operations[i]=+1  
                t=a+operations[i] 
                a=t 
        return t        

        