class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        li=[]
        a=set(nums2)
        for i in range(len(nums1)):
            
            
        

            if nums1[i] in a:
                
                li.append(nums1[i])
                
        if len(li)==0:
            return -1
        return li[0]    
              
                
                      
        