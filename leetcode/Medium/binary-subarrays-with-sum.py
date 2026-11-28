// Problem: Binary Subarrays With Sum
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/binary-subarrays-with-sum/
// Solved on: 2026-11-28T09:28:18.648Z

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        fq = {0:1}
        ans = 0
        prefix = 0
        
        for i in nums:
            prefix += i
            
            ans += fq.get(prefix - goal, 0)
            
            fq[prefix] = fq.get(prefix, 0) + 1
        return ans