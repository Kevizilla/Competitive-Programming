// Problem: Subarray Sums Divisible by K
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/subarray-sums-divisible-by-k/
// Solved on: 2026-11-28T09:37:03.019Z

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        fq = {0 : 1}
        ans = 0
        prefix = 0
        
        for i in nums:
            prefix += i
            r = prefix % k
            
            ans += fq.get(r, 0)
            
            fq[r] = fq.get(r, 0) + 1
        return ans