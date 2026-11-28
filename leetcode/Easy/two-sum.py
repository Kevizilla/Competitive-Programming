// Problem: Two Sum
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/two-sum/
// Solved on: 2026-11-28T09:41:35.014Z

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            required = target - nums[i]
            if required in d:
                return [d[required], i]
            if nums[i] not in d:
                d[nums[i]] = i

        return [-1]
