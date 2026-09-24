# 167. Two Sum II – Input Array Is Sorted

Given a 1-indexed array sorted in non-decreasing order, return the indices of the two numbers that add up to `target`, using only constant extra space.

### Your Solution

```python
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
```

- **Time:** O(n). Each iteration moves one pointer inward.
- **Space:** O(1). Only two indices are stored.

### Optimal Solution

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            if s < target:
                l += 1
            else:
                r -= 1
        return []
```

- **Time:** O(n)
- **Space:** O(1)

### Comparison

| | Your Solution | Optimal Solution |
|---|---|---|
| Approach | Two pointers from both ends | Two pointers from both ends |
| Time | O(n) | O(n) |
| Space | O(1) | O(1) |
| Improvement | — | None needed. Your solution is already optimal; this version only adds a fallback `return []` |

### Key Takeaway

In a sorted array, one comparison is enough to rule out a pointer. If the sum is too small, the left value can't pair with anything still in range, so move `l` right. If it's too big, move `r` left. Use this two-pointer approach instead of a hash map whenever the input is sorted and the problem asks for O(1) space.