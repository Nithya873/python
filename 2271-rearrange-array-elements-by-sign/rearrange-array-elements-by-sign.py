class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        arr=[0]*n
        pos=0
        neg=1
        for i in range(len(nums)):
            if nums[i]>=0:
                arr[pos]=nums[i]
                pos+=2
            else:
                arr[neg]=nums[i]
                neg+=2
        return arr


        
        


        