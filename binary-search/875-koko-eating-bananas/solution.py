"""
875. Koko Eating Bananas
LeetCode #875 |  https://leetcode.com/problems/koko-eating-bananas/
Difficulty: Easy | Medium | Hard

Approach: <one line on the key idea>
Time:  O(nlog(n))
Space: O(n)
"""


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        _min = 1
        _max = max(piles)

        while _min <= _max:

            m = (_min + _max) // 2
            total_time = sum((p + m - 1) // m for p in piles)

            if total_time > h:
                _min = m + 1
            else:
                _max = m - 1

        return _min



if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
