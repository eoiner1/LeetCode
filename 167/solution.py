class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [l+1, r+1]