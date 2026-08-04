"""
Reorder List
LeetCode #143  |  https://leetcode.com/problems/reorder-linked-list/
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
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return None

        first = head
        last = None

        #Step 1: Get the middle of the Linked List
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        last = slow.next #Prioritize first lst to have more nodes
        slow.next = None #Break the cycle at the half node


        #Step 2: Reverse the second half of the Linked List 
        prev = None
        while last:
            last.next, last, prev = prev, last.next, last

        last = prev
        #Step 3: Modify in place the Linked List accordingly.
        while first and last:
            # Step 1: Attach left to last
            first.next, first = last, first.next

            #Step 2: Attach last to the next first
            last.next, last = first, last.next


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
