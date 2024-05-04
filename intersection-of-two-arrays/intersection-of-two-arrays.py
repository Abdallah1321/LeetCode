class Solution(object):
    def intersection(self, nums1, nums2):
        intersection = set()
        for i in range(0, len(nums1)):
            for y in range(0,len(nums2)):
                if (nums1[i] == nums2[y] ):
                    intersection.add(nums1[i])
        
        return intersection
                
                
        