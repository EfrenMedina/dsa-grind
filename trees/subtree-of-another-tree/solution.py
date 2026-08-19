"""
572. Subtree of Another Tree
LeetCode #<n>  |  https://leetcode.com/problems/subtree-of-another-tree/
Difficulty: Easy 

Approach: <one line on the key idea>
Time:  O(m * n)
Space: O(m + n)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False

        ans = False

        if root and subRoot and root.val == subRoot.val:
            ans = self.sameTree(root, subRoot)
        
        if ans:
            return True
        else:
            ans = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return ans
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        elif root and not subRoot:
            return False
        else:
            if root.val == subRoot.val:
                return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
            else:
                return False


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
