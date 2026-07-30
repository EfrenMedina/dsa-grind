"""
121. Best Time to Buy and Sell Stock
LeetCode #121  |  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy

Approach: <one line on the key idea>
Time:  O(n)
Space: O(1)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        _min = math.inf
        result = 0

        for p in prices:
            _min = min(p, _min)
            result = max(p - _min, result)

        return max(0, result)


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
