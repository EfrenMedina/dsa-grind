"""
424. Longest Repeating Character Replacement
LeetCode #<n>  |  https://leetcode.com/problems/longest-repeating-character-replacement/
Difficulty: Medium

Approach: <one line on the key idea>
Time:  O(n)
Space: O(m)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        L = 0
        count = [0] * 26
        ans = 0
        top = 0

        for R in range(len(s)):
            current = ord(s[R]) - 65
            count[current] += 1
            if count[current] > count[top]:
                top = current

            if (R - L + 1 - count[top]) > k:
                count[ord(s[L]) - 65] -= 1
                L += 1
            
            if R - L + 1 > ans:
                ans = R - L + 1
        
        return ans
            
        

if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
