class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        li=[]
        n=len(nums)
        ns=set(nums)
        for i in range(1,n+1):
            if i not in ns:
                li.append(i)
        return li        
        