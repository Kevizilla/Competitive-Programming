// Problem: Continuous Subarray Sum
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/continuous-subarray-sum/
// Solved on: 2026-11-28T09:36:44.933Z

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        fq = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            r = prefix % k

            if r in fq:
                if i - fq[r] >= 2:
                    return True
            else:
                fq[r] = i

        return False