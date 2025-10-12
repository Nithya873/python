class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hs=sorted(heights)
        c=0
        for i in range(len(heights)):
        
            if heights[i]!=hs[i]:
                c+=1
        return c            

       
               

        