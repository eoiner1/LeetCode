# 977. Squares of a Sorted Array

Given an integer array sorted in non-decreasing order, return the squares of each number, also sorted in non-decreasing order.

### Your Solution

```python
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i, n in enumerate(nums):
            nums[i] = n ** 2
        return sorted(nums)
```

- **Time:** O(n log n). The sort dominates.
- **Space:** O(n). `sorted()` returns a new list and Timsort uses an extra buffer. Note that this version also changes the input list.

### Optimal Solution

```python
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        for k in range(n - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                res[k] = nums[l] * nums[l]
                l += 1
            else:
                res[k] = nums[r] * nums[r]
                r -= 1
        return res
```

- **Time:** O(n). Each step places one element.
- **Space:** O(1) extra, not counting the output array.

### Comparison

| | Your Solution | Optimal Solution |
|---|---|---|
| Approach | Square every element, then sort | Two pointers from both ends, fill from the back |
| Time | O(n log n) | O(n) |
| Space | O(n) | O(1) extra (O(n) including the output) |
| Improvement | — | Uses the input's sorted order: the largest square is always at one end, so no sort is needed |

### Key Takeaway

When the input is sorted, the largest absolute values are at the two ends. Compare the ends, write the larger square into the last open slot of the result, and move that pointer inward. If the input is already sorted and the question asks for sorted output, look for an O(n) two-pointer merge before reaching for a sort.