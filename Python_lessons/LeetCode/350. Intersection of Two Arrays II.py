class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        if len(nums1) < len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    result.append(nums2.pop(nums2.index(nums1[i])))
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    result.append(nums1.pop(nums1.index(nums2[i])))
        return result