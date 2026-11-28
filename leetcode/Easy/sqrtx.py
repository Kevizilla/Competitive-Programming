// Problem: Sqrt(x)
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/sqrtx/
// Solved on: 2026-11-28T09:41:55.640Z

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 0
        right = x // 2

        while left <= right:
            mid = (left + right)//2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return right
