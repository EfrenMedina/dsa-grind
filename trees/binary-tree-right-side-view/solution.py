"""
199. Binary Tree Right Side View
LeetCode #199 |  https://leetcode.com/problems/binary-tree-right-side-view/
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
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        
        ans = []
        queue = deque()

        if root:
            queue.append(root)
            ans.append(root.val)
        
        while len(queue) > 0:

            for _ in range(len(queue)):

                current = queue.popleft()

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            if len(queue) > 0:
                ans.append(queue[-1].val)
        return ans


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
