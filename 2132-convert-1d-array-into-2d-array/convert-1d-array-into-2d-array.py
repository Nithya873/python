class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        r=len(original)
        
        
        if r!=m*n:
            return []
        else:

            result=[]
            for i in range(m):
                row=[]
                for j in range(n):
                    row.append(0)
                result.append(row)  

            index=0
            for l in range(m):
                for k in range(n):
                    newr=index//n
                    newc=index%n
                    result[newr][newc]=original[index]
                    index+=1
            return result        

           
                

        