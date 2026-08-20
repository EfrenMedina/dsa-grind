"""
102. Binary Tree Level Order Traversal
LeetCode #102  |  https://leetcode.com/problems/binary-tree-level-order-traversal/
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

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        
        ans = []
        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            current_level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                current_level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(current_level)
        return ans




if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
