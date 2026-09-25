# 42. Trapping Rain Water (Hard)

Given an elevation map of bar heights (width 1 each), compute how much rain water is trapped.

### Your Solution: Two Pointers ✅ Optimal
```python
class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water
```
- **Time:** O(n). Each index is visited once as the pointers move toward each other.
- **Space:** O(1). Only four scalar variables.

### Optimal Solution
Same as above. O(n) time is the lower bound because every bar must be read, and O(1) extra space is the minimum.

Alternative approaches, for reference:

| Approach | Time | Space |
|---|---|---|
| Brute force (scan left/right max per index) | O(n²) | O(1) |
| Prefix/suffix max arrays | O(n) | O(n) |
| Monotonic stack | O(n) | O(n) |
| **Two pointers** | **O(n)** | **O(1)** |

### Comparison
| | Your Solution | Optimal Solution |
|---|---|---|
| Approach | Two pointers with running maxes | Same |
| Time | O(n) | O(n) |
| Space | O(1) | O(1) |
| Improvement | — | None needed. Already optimal. |

### Key Takeaway
The water above bar i is `min(maxLeft, maxRight) - height[i]`. When the left bar is shorter than the right bar, there is already a wall at least as tall on the right. So `left_max` alone sets the water level at `left`, and you never need the exact right max. Always move the pointer on the shorter side.