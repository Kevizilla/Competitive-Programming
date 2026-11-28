// Problem: Intersection of Two Arrays
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/intersection-of-two-arrays/
// Solved on: 2026-11-28T09:43:30.932Z

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))