class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=0
        r=0
        d=0
        for i in moves:
            if i=="L":
                l+=1
            elif i=="R":
                r+=1
            elif i=="_":
                d+=1
        if l>r:
            l+=d
        else:
            r+=d    
    
            
        return abs(r-l)       


               
        