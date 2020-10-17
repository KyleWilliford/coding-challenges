"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/

Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the
nodes of the first two lists.

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            lSmall = l1
            lLarge = l2
        else:
            lSmall = l2
            lLarge = l1
        # print(f'lSmall, lLarge = {lSmall, lLarge}')
        head = lSmall
        node = lLarge
        # print(f'head, node = {head, node}')
        while node:
            if not lSmall.next:
                # print(f'lSmall, node = {lSmall, node}')
                lSmall.next = node
                break
                # print(f'lSmall = {lSmall}')
            elif lSmall.val <= node.val <= lSmall.next.val:
                temp = node.next
                node.next = lSmall.next
                lSmall.next = node
                lSmall = node
                node = temp
            else:
                lSmall = lSmall.next

            # print(f'node = {node}, l2 = {l2}')

        # print(f'head = {head}')
        return head
