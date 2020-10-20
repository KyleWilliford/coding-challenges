"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from src.main.python.utility.linked_list import ListNode, initialLinkedList


class Solution:
    def reverseList_iterative(self, head: ListNode) -> ListNode:
        """
        iteratively

        Runtime: 32 ms. Your runtime beats 89.08 % of python3 submissions.
        Memory Usage: 15.3 MB
        :param head:
        :return:
        """
        priorNode = None
        currNode = head
        while currNode:
            nextNode = currNode.next
            currNode.next = priorNode
            priorNode = currNode
            currNode = nextNode

        return priorNode

    def reverseList_recursive(self, head: ListNode) -> ListNode:
        """
        recursively

        :param head:
        :return:
        """
        if not node:
            return None
        node = self.reverseList_recursive(node.next)
