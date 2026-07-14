"""
Two Sum
LeetCode #1  |  https://leetcode.com/problems/two-sum/
Difficulty: Easy

Approach: one pass, store each value's index in a hash map; for every number
check whether its complement (target - num) was already seen.
Time:  O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    print("ok")
