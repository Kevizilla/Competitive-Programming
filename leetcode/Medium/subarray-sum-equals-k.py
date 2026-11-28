// Problem: Subarray Sum Equals K
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/subarray-sum-equals-k/
// Solved on: 2026-11-28T09:37:38.897Z

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        fq = {0: 1}
        prefix = 0
        ans = 0
        
        for i in nums:
            prefix += i
            
            ans += fq.get(prefix - k, 0)
            
            fq[prefix] = fq.get(prefix, 0) + 1
        
        return ans
        