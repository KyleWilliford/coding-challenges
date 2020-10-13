"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        One pass with two pointers

        Runtime: 28 ms, faster than 91.73% of Python3 online submissions for Remove Nth Node From End of List.
        Memory Usage: 14.2 MB, less than 99.98% of Python3 online submissions for Remove Nth Node From End of List.
        :param head:
        :param n:
        :return:
        """
        node = head
        cnt = 1
        nodeToDelete = None
        nodePrior = None
        while node:
            if cnt == n:
                nodeToDelete = head
            elif cnt > n:
                nodePrior = nodeToDelete
                nodeToDelete = nodeToDelete.next
            node = node.next
            cnt += 1

        if nodeToDelete == head and not nodeToDelete.next:
            return None
        elif nodeToDelete == head:
            head = nodeToDelete.next
        else:
            nodePrior.next = nodeToDelete.next
        return head
