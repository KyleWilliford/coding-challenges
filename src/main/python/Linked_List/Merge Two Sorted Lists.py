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
        head = l2
        node = l1
        while node:
            if l2.val <= node.val <= l2.next.val:
                temp = node.next
                node.next = l2.next
                l2.next = node
                l2 = node
                node = temp
            else:
                l2 = l2.next

            print(f'node = {node}, l2 = {l2}')

        print(f'head = {head}')
        return head

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(f'l1 = {l1}, l2 = {l2}')
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            head = l1
        else:
            head = l2
        print(f'head = {head}')
        tail = head
        print(f'tail = ={tail}')
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
                print(f'l1 = {l1}, l2 = {l2}')
            else:
                tail.next = l2
                l2 = l2.next
            print(f'head, tail = {head, tail}, l1 = {l1}, l2 = {l2}')
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        print(f'head, tail = {head, tail}, l1 = {l1}, l2 = {l2}')
        return head