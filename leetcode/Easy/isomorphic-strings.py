// Problem: Isomorphic Strings
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/isomorphic-strings/
// Solved on: 2026-11-28T09:40:58.356Z

class Solution:
    def isIsomorphic(self, s, t):
        sd = {}
        td = {}

        for a, b in zip(s, t):
            if a in sd and sd[a] != b:
                return False

            if b in td and td[b] != a:
                return False

            sd[a] = b
            td[b] = a

        return True