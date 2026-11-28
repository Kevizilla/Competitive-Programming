// Problem: Sort Characters By Frequency
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/sort-characters-by-frequency/
// Solved on: 2026-11-28T09:41:18.549Z

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        fq = Counter(s)
        sorted_dic = dict(sorted(fq.items(), key=lambda x:x[1], reverse=True))
        ans = ""
        for i in sorted_dic:
            ans += i * sorted_dic[i]

        return ans