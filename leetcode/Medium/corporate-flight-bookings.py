// Problem: Corporate Flight Bookings
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/corporate-flight-bookings/
// Solved on: 2026-11-28T09:40:38.100Z

class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        ans = [0] * (n+1)
        for i in bookings:
            ans[i[0] - 1] += i[2]
            ans[i[1]] -= i[2]

        prefix = [0]
        for i in ans:
            prefix.append(prefix[-1] + i)
        
        return prefix[1:-1]