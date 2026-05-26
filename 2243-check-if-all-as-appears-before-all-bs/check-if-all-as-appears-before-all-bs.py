class Solution:
    def checkString(self, s: str) -> bool:
        n=list(s)
        li=[]
        for i in range(len(n)):
            if n[i]=="a":
                li.append(1)
            if n[i]=="b" :
                li.append(2)
        c=0          
        for j in range(len(li)-1):
            if li[j]>li[j+1]:
                c+=1
        if c>=1:
            return False  
        return True           

