// Problem: Intersection of Two Arrays II
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/intersection-of-two-arrays-ii/
// Solved on: 2026-11-28T09:43:18.313Z

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq = {}
        ans = []

        for x in nums1:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        for x in nums2:
            if x in freq and freq[x] > 0:
                ans.append(x)
                freq[x] -= 1

        return ans