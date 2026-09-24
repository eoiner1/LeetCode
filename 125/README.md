# 125. Valid Palindrome

Return true if `s` reads the same forwards and backwards after converting it to lowercase and removing everything except letters and digits.

### Your Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else: 
                return False
        return True
        
```

- **Time:** O(n). Building the lowercase copy is O(n), and the loop runs at most n times.
- **Space:** O(n). `s.lower()` creates a full copy of the string.

### Optimal Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True
```

- **Time:** O(n). Each character is visited at most once.
- **Space:** O(1). Only two indices are stored.

### Comparison

| | Your Solution | Optimal Solution |
|---|---|---|
| Approach | Two pointers on a lowercased copy | Two pointers in place, lowercase each character on compare |
| Time | O(n) | O(n) |
| Space | O(n) | O(1) |
| Improvement | — | Drops the `s.lower()` copy and lowercases each character only when comparing, which cuts space from O(n) to O(1) |

### Key Takeaway

For palindrome checks with ignored characters, don't clean the string first. Walk two pointers inward, skip invalid characters as you go, and normalize each character only at the moment you compare it. That gives O(n) time with O(1) space.