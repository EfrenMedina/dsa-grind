"""
206. Reverse Linked List
LeetCode #206  |  https://leetcode.com/problems/reverse-linked-list"
Difficulty: Easy 

Approach: <one line on the key idea>
Time:  O(n)
Space: O(1)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        prev = None
        curr = head
        temp = None
        while curr.next is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        
        curr.next = prev
        return curr


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
