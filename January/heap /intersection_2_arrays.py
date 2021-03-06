#  Question 4. ​https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                
                i += 1
                j += 1
                
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
                
        return result