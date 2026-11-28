// Problem: Search in Rotated Sorted Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
// Solved on: 2026-11-28T09:10:33.541Z

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)

        if n == 0:
            return -1

        l, r = 0, n - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        def binary_search(left, right):
            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        idx = binary_search(pivot, n)

        if idx < n and nums[idx] == target:
            return idx

        idx = binary_search(0, pivot)

        if idx < pivot and nums[idx] == target:
            return idx

        return -1