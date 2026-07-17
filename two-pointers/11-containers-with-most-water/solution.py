"""
11. Container With Most Water
LeetCode #11  |  https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium

Approach: <one line on the key idea>
Time:  O(n)
Space: O(1)
"""


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        
        L = 0
        R = len(heights) - 1

        result = 0
        while L < R:
            current = (R - L) * min(heights[R], heights[L])
            result = max(result, current)
            if heights[L] < heights[R]:
                L += 1
            else: 
                R -= 1
        return result




if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
