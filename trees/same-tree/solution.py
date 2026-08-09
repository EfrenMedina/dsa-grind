"""
100. Same Tree
LeetCode #100  |  https://leetcode.com/problems/same-tree/
Difficulty: Easy | Medium | Hard

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if int(not p) != int(not q):
            return False
        elif not p and not q:
            return True
        elif p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
