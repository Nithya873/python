class Solution:
    def largestInteger(self, num: int) -> int:
        li=[int(i) for i in str(num)]
        e=[]
        o=[]
        for i in range(len(li)):
            if li[i]%2==0:
                e.append(li[i])
            else:
                o.append(li[i])    
        e.sort(reverse=True)
        o.sort(reverse=True)
        res=[]
        for i in li:
            if i%2==0:
                res.append(e.pop(0))
            else:
                res.append(o.pop(0))
        return int("".join(map(str, res)))            