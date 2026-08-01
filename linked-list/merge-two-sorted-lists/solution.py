"""
21. Merge Two Sorted Lists
LeetCode #21  |  https://leetcode.com/problems/merge-two-sorted-lists/
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = None
        curr = None

        while list1 and list2:
            if curr is None:
                if list1.val < list2.val:
                    curr = list1
                    ans = curr
                    list1 = list1.next
                else:
                    curr = list2
                    ans = curr
                    list2 = list2.next
                continue

            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
            
        
        if list1:
            if not ans:
                return list1
            curr.next = list1
        else:
            if not ans:
                return list2
            curr.next = list2
        
        return ans            


if __name__ == "__main__":
    s = Solution()
    # quick sanity checks
    # assert s.solve(...) == expected
    print("ok")
