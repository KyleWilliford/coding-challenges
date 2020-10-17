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
        """
        Runtime: 36 ms. Your runtime beats 77.61 % of python3 submissions.
        Memory Usage: 14.2 MB
        :param l1:
        :param l2:
        :return:
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        # print(f'l1, l2 = {l1, l2}')
        head = l1
        node = l2
        # print(f'head, node = {head, node}')
        while node:
            if not l1.next:
                # print(f'l1, node = {l1, node}')
                l1.next = node
                break
                # print(f'l1 = {l1}')
            elif l1.val <= node.val <= l1.next.val:
                temp = node.next
                node.next = l1.next
                l1.next = node
                l1 = node
                node = temp
            else:
                l1 = l1.next

            # print(f'node = {node}, l2 = {l2}')

        # print(f'head = {head}')
        return head
