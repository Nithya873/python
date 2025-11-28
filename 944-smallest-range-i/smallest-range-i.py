class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        mx = max(nums)
        mn = min(nums)
        diff = mx - mn
        return max(0, diff - 2 * k)    
                    

                    


        