"""
167. Two Sum II - Input Array Is Sorted
LeetCode #<n>  |  https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Difficulty: Medium 

Approach: <one line on the key idea>
Time:  O(n)
Space: O(1)
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
