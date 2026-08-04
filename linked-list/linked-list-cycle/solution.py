"""
Linked List Cycle
LeetCode #141  |  https://leetcode.com/problems/linked-list-cycle//
Difficulty: Easy | Medium | Hard

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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            
            if slow is fast:
                return True
            
            slow = slow.next
            fast = fast.next.next

        return False


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
