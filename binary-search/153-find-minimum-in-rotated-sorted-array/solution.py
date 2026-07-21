"""
153. Find Minimum in Rotated Sorted Array
LeetCode #<n>  |  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Difficulty: Easy | Medium | Hard

Approach: <one line on the key idea>
Time:  O(log(n))
Space: O(1)
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
