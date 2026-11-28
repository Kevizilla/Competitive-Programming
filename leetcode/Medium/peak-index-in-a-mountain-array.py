// Problem: Peak Index in a Mountain Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/peak-index-in-a-mountain-array/
// Solved on: 2026-11-28T13:03:33.728Z

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l = 0
        r = len(arr) - 1

        while l < r:
            mid = (l + r) // 2

            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l