// Problem: Spiral Matrix
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/spiral-matrix/
// Solved on: 2026-11-28T09:38:20.987Z


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # top
            ans.extend(matrix[top][left:right+1])
            top += 1

            # right
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1

            # bottom
            if top <= bottom:
                x = matrix[bottom][left:right+1]
                ans.extend(reversed(x))
                bottom -= 1

            # left
            if left <= right:
                for j in range(bottom, top-1, -1):
                    ans.append(matrix[j][left])
                left += 1

        return ans
