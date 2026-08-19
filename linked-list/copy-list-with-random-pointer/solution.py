"""
138. Copy List with Random Pointer
LeetCode #138  |  https://leetcode.com/problems/copy-list-with-random-pointer/
Difficulty: Medium 

Approach: <one line on the key idea>
Time:  O(n)
Space: O(m)
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        node_map = {}

        curr = head
        while curr:
            node_map[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        curr = head
        
        while curr:
            copy = node_map[curr]
            copy.next = node_map.get(curr.next)
            copy.random = node_map.get(curr.random)
            curr = curr.next
        
        return node_map.get(head)

if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
