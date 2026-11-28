// Problem: Monotonic Array
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/monotonic-array/
// Solved on: 2026-11-28T09:43:09.396Z

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        s = sorted(nums)
        return True if nums == s or nums == s[::-1] else False