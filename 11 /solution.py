class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater = 0
        l, r = 0, len(height) - 1
        while l < r:
            water = (min(height[l], height[r])) * (r-l)
            maxWater = max(water, maxWater)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxWater
