"""
704. Binary Search
LeetCode #<n>  |  https://leetcode.com/problems/binary-search/
Difficulty: Easy 

Approach: <one line on the key idea>
Time:  O(log(n))
Space: O(1)
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        L = 0
        R = len(nums) - 1

        while L <= R:
            m = (L + R) // 2

            if nums[m] > target:
                R = m - 1
            elif nums[m] < target:
                L = m + 1
            else:
                return m
        return -1


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
