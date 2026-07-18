"""
739. Daily Temperatures
LeetCode 739  |  https://leetcode.com/problems/daily-temperatures/
Difficulty: Medium

Approach: <one line on the key idea>
Time:  O(n)
Space: O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, index = stack.pop()
                result[index] = i - index
            stack.append((t, i))
        return result


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
