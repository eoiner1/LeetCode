class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i, n in enumerate(nums):
            nums[i] = n ** 2
        return sorted(nums)
