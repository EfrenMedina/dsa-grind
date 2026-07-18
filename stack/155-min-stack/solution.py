"""
155. Min Stack
LeetCode #155  |  https://leetcode.com/problems/min-stack/
Difficulty: Medium

Approach: <one line on the key idea>
Time:  O(1)
Space: O(n)
"""


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            if val < current_min:
                self.stack.append((val, val))
            else:
                self.stack.append((val, current_min))

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        



if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
