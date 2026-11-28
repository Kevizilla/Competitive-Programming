// Problem: Minimum Value of Merged Integers
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/minimum-value-of-merged-integers/
// Solved on: 2026-11-28T09:38:59.654Z

class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        arr = []
        for i in range(0, len(nums), 2):
            cur = str(nums[i])
            cur += str(nums[i+1])
            arr.append(int(cur))
        
        return min(arr)


# x = Solution()
