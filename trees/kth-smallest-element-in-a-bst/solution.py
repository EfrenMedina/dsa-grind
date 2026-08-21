"""
230. Kth Smallest Element in a BST
LeetCode #230  |  https://leetcode.com/problems/kth-smallest-element-in-a-bst/
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.k = k

        if not root:
            return None
        
        ans = self.kthSmallest(root.left, self.k)

        if ans is not None:
            return ans

        self.k -= 1
        
        if self.k == 0:
            return root.val

        if ans is not None:
            return ans
        else:
            return self.kthSmallest(root.right, self.k)
        


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
