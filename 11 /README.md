# 11. Container With Most Water

Given line heights, pick two lines that, together with the x-axis, form a container holding the most water.

### Your Solution

```python
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
```

- **Time:** O(n). Each iteration moves one pointer inward.
- **Space:** O(1)

### Optimal Solution

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0
        while l < r:
            h = min(height[l], height[r])
            best = max(best, h * (r - l))
            while l < r and height[l] <= h:
                l += 1
            while l < r and height[r] <= h:
                r -= 1
        return best
```

- **Time:** O(n)
- **Space:** O(1)

### Comparison

| | Your Solution | Optimal Solution |
|---|---|---|
| Approach | Two pointers, move the shorter line | Two pointers, move the shorter line, skip lines no taller than the current level |
| Time | O(n) | O(n) |
| Space | O(1) | O(1) |
| Improvement | — | None needed. The skip loops only save constant-factor work by not measuring containers that can't be bigger |

### Key Takeaway

Start with the widest container and always move the pointer at the shorter line. The shorter line caps the water level, so pairing it with any closer line gives a narrower container that is no taller. Discarding it can never lose the best answer.