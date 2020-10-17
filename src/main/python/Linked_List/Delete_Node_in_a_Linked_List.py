"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/

Delete Node in a Linked List
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead
 you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Constraints:

The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node to be deleted is in the list and is not a tail node
"""
from src.main.python.utility.linked_list import ListNode

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
