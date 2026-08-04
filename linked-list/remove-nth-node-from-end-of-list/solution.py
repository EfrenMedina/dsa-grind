"""
Remove Nth Node From End of List
LeetCode #19  |  https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Difficulty: Medium

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #Step 1: Get the lenght of the Linked List
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        #Edge Case: Removing first
        if length == n:
            return head.next

        #Step 2: Simpli remove nth-adjusted node
        nReverse = length - n - 1        
        curr = head
        while curr:
            if nReverse == 0:
                curr.next = curr.next.next
                return head
            curr = curr.next
            nReverse -= 1



if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
