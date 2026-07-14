"""
128. Longest Consecutive Sequence
LeetCode #<n>  |  https://leetcode.com/problems/longest-consecutive-sequence
Difficulty: Medium

Approach: <one line on the key idea>
Time:  O(n)
Space: O(n)
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        numSet = set(nums)

        result = 0
        for num in numSet:
            if num - 1in numSet:
                continue
            current_streak = 1
            while num + current_streak in numSet:
                current_streak += 1
            result = max(result, current_streak)
        return result
        


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
