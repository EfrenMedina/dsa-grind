"""
236. Lowest Common Ancestor of a Binary Tree
LeetCode #<n>  |  https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Difficulty: Medium

Approach: <one line on the key idea>
Time:  O(n)
Space: O(n)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or root is p or root is q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        if left:
            return left
        else:
            return right


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
