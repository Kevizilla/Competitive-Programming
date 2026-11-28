// Problem: Spiral Matrix II
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/spiral-matrix-ii/
// Solved on: 2026-11-28T09:37:59.097Z


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        while top <= bottom and left <= right:

            # top
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1

            # right
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # bottom
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1
                bottom -= 1

            # left
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        return matrix
