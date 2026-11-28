// Problem: Maximum Subarray
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/maximum-subarray/
// Solved on: 2026-11-28T09:39:13.206Z

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maximum = nums[0]
        cur_max = nums[0]

        for i in nums[1:]:
            cur_max = max(cur_max + i, i)
            maximum = max(maximum, cur_max)
        return maximum

