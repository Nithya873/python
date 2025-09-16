class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_num={}
        for i in nums:
            if i in count_num:
                count_num[i]+=1
            else:
                count_num[i]=1
        for i,count in count_num.items():
            if count==1:
                return i           
        