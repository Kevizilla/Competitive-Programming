// Problem: Koko Eating Bananas
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/koko-eating-bananas/
// Solved on: 2026-11-28T09:43:00.096Z

from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = max(piles)+1
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if sum(ceil(i/mid) for i in piles) <= h:
                right = mid - 1
                hour = mid
            else:
                left = mid + 1

        return hour
        