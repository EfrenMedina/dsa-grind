"""
20. Valid Parentheses
LeetCode #20  |  https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy

Approach: <one line on the key idea>
Time:  O(n)
Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        if len(s) <= 1:
            return False
        for c in s:

            if c in '({[':
                stack.append(c)
            elif stack == []:
                return False
            else:
                if not (c == ')' and stack[-1] == '(' or
                        c == '}' and stack[-1] == '{' or
                        c == ']' and stack[-1] == '['):
                    return False
                stack.pop()
        return stack == []


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
