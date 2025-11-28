class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                ng=-1
                if nums1[i]==nums2[j]:
                    for k in range(j+1,len(nums2)):
                        if nums2[k]>nums1[i]:
                            ng=nums2[k]
                            break
                    l.append(ng)
                    break
        return l     

                  
                    
        
        