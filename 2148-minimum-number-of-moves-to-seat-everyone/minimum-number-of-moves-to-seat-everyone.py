class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        li=[]
        x=sorted(seats)
        e=sorted(students)
        for i in range(len(x)):
            c=abs(e[i]-x[i])
            li.append(c)
        k=sum(li) 
        if k<0:
            return abs(k)   
        return  sum(li)    

        
        