class Solution:
    def reverseWords(self, s: str) -> str:
        k=s[::-1]
        m=k.split()
        l=m[::-1]
        return " ".join(l)
       
        
        