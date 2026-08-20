"""
1448. Count Good Nodes in Binary Tree
LeetCode #1448  |  https://leetcode.com/problems/count-good-nodes-in-binary-tree/
Difficulty: Easy | Medium | Hard

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

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ans = 0
        queue = deque()

        if root:
            queue.append((root, root.val))
        
        while len(queue) > 0:

            for _ in range(len(queue)):

                current, _max = queue.popleft()
                if current.val >= _max:
                    ans += 1

                if current.left:
                    queue.append((current.left, max(_max, current.val)))
                if current.right:
                    queue.append((current.right, max(_max, current.val)))

        return ans
        


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
