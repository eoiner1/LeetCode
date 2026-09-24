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
