class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=max(candies)
        li=[]
        for i in range(len(candies)):
            candies[i]+=extraCandies
            li.append(candies[i])
        for j in range(len(li)):
            if li[j]>=a:
                li[j]=True
            elif li[j]<a:    

                li[j]=False
        return li
                  

        