// Problem: Reverse Vowels of a String
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/reverse-vowels-of-a-string/
// Solved on: 2026-11-28T09:41:44.837Z

class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        ls = list(s)
        while left < right:
            if s[left] not in "aeiouAEIOU" and s[right] not in "aeiouAEIOU":
                left += 1
                right -= 1
            elif s[left] not in "aeiouAEIOU":
                left += 1
            elif s[right] not in "aeiouAEIOU":
                right -= 1
            else:
                ls[left], ls[right] = ls[right], ls[left]
                left += 1
                right -= 1
        return "".join(ls)
