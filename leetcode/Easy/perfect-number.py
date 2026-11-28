// Problem: Perfect Number
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/perfect-number/
// Solved on: 2026-11-28T09:35:17.281Z

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        ans = 1
        if num == 1:
            return False
        for i in range(2, int(num **.5)+1):
            if num % i == 0:
                ans += i
                if i != num // i:
                    ans += num // i

        if ans == num:
            return True
        else:
            return False
