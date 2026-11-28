// Problem: Product of Array Except Self
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/product-of-array-except-self/
// Solved on: 2026-11-28T05:14:48.136Z

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []

        prefix = [1]
        for i in nums:
            prefix.append(prefix[-1] * i)
        suffix = [1]
        for i in nums[::-1]:
            suffix.append(suffix[-1] * i)

        for i in range(n):
            ans.append(prefix[i] * suffix[n-i-1])

        return ans