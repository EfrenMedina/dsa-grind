"""
150. Evaluate Reverse Polish Notation
LeetCode #150  |  https://leetcode.com/problems/evaluate-reverse-polish-notation/
Difficulty: Medium

Approach: <one line on the key idea>
Time:  O(n)
Space: O(n)
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        num_q = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                right = num_q.pop()
                left = num_q.pop()

                if token == '+':
                    num_q.append(left + right) 
                elif token == '-':
                    num_q.append(left - right) 
                elif token == '*':
                    num_q.append(left * right) 
                else:
                    result = num_q.append(int(left / right))
            else:
               num_q.append(int(token)) 
        return num_q.pop()


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
