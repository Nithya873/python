class Solution:
    def finalString(self, s: str) -> str:
        k=[]
        for i  in s:
            if i!="i":
                k.append(i)
            elif i=="i":
                k=k[::-1]
        return "".join(k)       



        

        


        