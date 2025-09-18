class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        nums2_copy=nums2.copy()
        for i in nums1:

            if i in nums2_copy:
                l.append(i)
                nums2_copy.remove(i)
        return  l        