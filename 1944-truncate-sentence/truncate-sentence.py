class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        m=s.split()
        o=m[:k]
        
        return " ".join(o)
          



        