// Problem: Contiguous Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/contiguous-array/
// Solved on: 2026-11-28T09:37:21.092Z

class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        fq = {0:-1}
        dif = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                dif -= 1
            else:
                dif += 1

            if dif in fq:
                ans = max(ans, i - fq[dif])
            else:
                fq[dif] = i
        return ans