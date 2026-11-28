// Problem: Longest Palindromic Substring
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/longest-palindromic-substring/
// Solved on: 2026-11-28T09:39:23.551Z

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        largest = 1
        n = len(s)

        # Check for even-length palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                cur_len = 2
                pointer1 = i - 1
                pointer2 = i + 2

                if cur_len > largest:
                    largest = cur_len
                    ans = s[i:i + 2]

                while pointer1 >= 0 and pointer2 < n:
                    if s[pointer1] == s[pointer2]:
                        cur_len += 2

                        if cur_len > largest:
                            largest = cur_len
                            ans = s[pointer1:pointer2 + 1]

                        pointer1 -= 1
                        pointer2 += 1
                    else:
                        break

        # Check for odd-length palindromes
        for j in range(1, n - 1):
            if s[j - 1] == s[j + 1]:
                cur_len = 3
                pointer1 = j - 2
                pointer2 = j + 2

                if cur_len > largest:
                    largest = cur_len
                    ans = s[j - 1:j + 2]

                while pointer1 >= 0 and pointer2 < n:
                    if s[pointer1] == s[pointer2]:
                        cur_len += 2

                        if cur_len > largest:
                            largest = cur_len
                            ans = s[pointer1:pointer2 + 1]

                        pointer1 -= 1
                        pointer2 += 1
                    else:
                        break

        return ans