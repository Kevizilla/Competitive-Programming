// Problem: Third Maximum Number
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/third-maximum-number/
// Solved on: 2026-11-28T09:43:43.233Z

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        unique_set = set(nums)
        if len(unique_set) < 3:
            return max(nums)
        unique = list(unique_set)
        return sorted(unique, reverse=True)[2]


