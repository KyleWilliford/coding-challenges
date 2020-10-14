"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList_interative(self, head: ListNode) -> ListNode:
        """
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