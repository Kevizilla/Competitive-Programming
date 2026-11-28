// Problem: Majority Element
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/majority-element/
// Solved on: 2026-11-28T09:39:46.486Z

from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        fq = Counter(nums)
        return max(fq, key=fq.get)