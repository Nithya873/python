class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        if m*n!=r*c:
            return mat
        result=[]
        for i in range(r):
            row=[]  
            for j in range(c):
                row.append(0)
            result.append(row) 
        index=0
        for k in range(m):
            for p in range(n):
                new_mat_r=index//c
                n_m_c=index%c
                result[new_mat_r][n_m_c]=mat[k][p]
                index +=1
        return result          

        

        

        