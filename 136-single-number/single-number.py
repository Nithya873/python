from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       count_map={}
       for i in nums:
        if i in count_map:
            count_map[i]+=1
        else:
            count_map[i] =1
       for i,count in count_map.items():
        if count==1:
            return i         


     