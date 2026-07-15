"""
125. Valid Palindrome
LeetCode #125  |  https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy 

Approach: <one line on the key idea>
Time:  O(n)
Space: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and j > i:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
