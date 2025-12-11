class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        a=0
        for i in range(len(arr1)):
            ok=True
            for j in range(len(arr2)):
                k=arr1[i]-arr2[j]
                if abs(k)<=d:
                    ok= False

                
            if ok:
                a+=1       
                    
        return a            
        