class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        li=[nums[0]]
        ni=[nums[1]]
        for i in range(2,len(nums)):
            
            if li[-1]>ni[-1]:
                li.append(nums[i])
            else:
                ni.append(nums[i])
       
    
        return li+ni

        