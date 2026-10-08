class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pi=[]
        ni=[]
        h=len(nums)
        for i in nums:
            if i>=0:
                pi.append(i)
            else:
                ni.append(i)
        ff=[]
        p=0
        n=0
        for j in range(h):
            if j%2==0:

                ff.append(pi[j//2])
                
            else:

                ff.append(ni[j//2])
                
        return ff

        
        


        