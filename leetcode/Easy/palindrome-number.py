// Problem: Palindrome Number
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/palindrome-number/
// Solved on: 2026-11-28T09:43:53.801Z

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]