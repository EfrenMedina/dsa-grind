"""
3. Longest Substring Without Repeating Characters
LeetCode #<n>  |  https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium 

Approach: <one line on the key idea>
Time:  O(n)
Space: O(1)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        indexes = {}
        result = 0
        l = 0

        for i, c in enumerate(s):
            
            if c not in indexes:
                indexes[c] = i
                result = max(result, i - l + 1)
            else:
                l = max(indexes[c] + 1, l)
                indexes[c] = i
                result = max(result, i - l + 1)
        return result


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
