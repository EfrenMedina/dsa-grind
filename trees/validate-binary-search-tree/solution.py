"""
98. Validate Binary Search Tree
LeetCode #98  |  https://leetcode.com/problems/validate-binary-search-tree/
Difficulty: Medium

Approach: <one line on the key idea>
Time:  O(n)
Space: O(n)
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST(root, -math.inf, math.inf)

    def validBST(self, root: Optional[TreeNode], lower: int, upper: int) -> bool:
        if not root:
            return True

        if not (lower < root.val < upper):
            return False
        else:
            return self.validBST(root.left, lower, root.val) and self.validBST(root.right, root.val, upper)


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
