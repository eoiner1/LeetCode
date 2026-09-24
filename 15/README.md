# 15. 3Sum

Return all unique triplets `[a, b, c]` from `nums` such that `a + b + c == 0`.

### Your Solution

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        sortedNums = sorted(nums)
        for index, num in enumerate(sortedNums):
            if index > 0 and sortedNums[index] == sortedNums[index-1]:
                continue
            if num > 0:
                return output
            l, r = index + 1, len(sortedNums) - 1
            while l < r:
                s = sortedNums[l] + sortedNums[r] + num
                if s == 0:
                    result = [num, sortedNums[l], sortedNums[r]]
                    output.append(result)
                    l += 1
                    while l < r and sortedNums[l] == sortedNums[l-1]:
                        l += 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return output
```

- **Time:** O(n²)
- **Space:** O(n) for the sorted copy

### Optimal Solution

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        n = len(nums)
        output = []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return output
```

- **Time:** O(n²)
- **Space:** O(n) for the sorted copy (O(1) extra if you sort in place)

### Comparison

| | Your Solution | Optimal Solution |
|---|---|---|
| Approach | Sort + two pointers + duplicate skipping | Sort + two pointers + duplicate skipping |
| Time | O(n²) | O(n²) |
| Space | O(n) | O(n) |
| Improvement | — | None needed. The only differences are style: `range(n - 2)`, `break` instead of `return` |

### Key Takeaway

3Sum is a loop over each `nums[i]` with a Two Sum II search inside it. After sorting, equal values sit next to each other, so skip a repeat of the previous value at both levels: in the outer loop, and for `l` after a match. Then no duplicate triplet is ever created. Stop the outer loop once `nums[i] > 0`, because nothing to its right can bring the sum back to zero.