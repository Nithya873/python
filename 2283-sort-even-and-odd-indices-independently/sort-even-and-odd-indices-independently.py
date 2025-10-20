class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for j in range(n):
            for i in range(n-2):
                if nums[i]>nums[i+2] and i%2==0:
                    nums[i],nums[i+2]=nums[i+2],nums[i]
                
                if i%2!=0 and nums[i+2]>nums[i]:
                    nums[i],nums[i+2]=nums[i+2],nums[i]
        return nums        
    

            

        


                

           

        