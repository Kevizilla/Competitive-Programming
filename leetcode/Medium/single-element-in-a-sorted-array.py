// Problem: Single Element in a Sorted Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python3
// Verdict: Accepted
// URL: https://leetcode.com/problems/single-element-in-a-sorted-array/
// Solved on: 2026-11-28T15:21:42.252Z

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == nums[mid - 1]:
                if (mid - 1 - l )% 2 == 1 and (mid - 1 - l ) != 0:
                    r = mid - 2
                else:
                    l = mid + 1
            elif nums[mid] == nums[mid + 1]:
                if (mid - l) % 2 == 1:
                    r = mid - 1
                else:
                    l = mid + 2
            else:
                return nums[mid]
        return nums[l]

