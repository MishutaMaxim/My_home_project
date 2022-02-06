class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                results.update({nums[i] + nums[j]: [i, j]})
        return results[target]