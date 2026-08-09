"""
104. Maximum Depth of Binary Tree
LeetCode #104  |  https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy 

Approach: <one line on the key idea>
Time:  O(log(n))
Space: O(1)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
