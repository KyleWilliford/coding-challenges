"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/

Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
"""
from src.main.python.utility.linked_list import ListNode, initialLinkedList_Cycle


class Solution:
    def hasCycle_hast(self, head: ListNode) -> bool:
        """
        Use hash table

        Runtime: 40 ms. Your runtime beats 97.79 % of python3 submissions.
        Memory Usage: 17.3 MB
        :param head:
        :return:
        """
        # print(head)
        nodeSet = set()
        node = head
        while node:
            if node not in nodeSet:
                nodeSet.add(node)
            else:
                return True
            node = node.next
        return False

    def hasCycle_2pointer(self, head: ListNode) -> bool:
        """
        Use two pointer

        Runtime: 44 ms. Your runtime beats 91.15 % of python3 submissions.
        Memory Usage: 17 MB
        :param head:
        :return:
        """
        if not head:
            return False
        node1 = head
        node2 = head
        # print(node1.val, node2.val)
        if not node2.next:
            return False
        while node2.next.next:
            # print(node1.val, node2.val)
            node1 = node1.next
            node2 = node2.next.next
            if node1 == node2:
                return True
            elif not node2.next:
                return False
        return False


# Tests


sol = Solution()
valList1 = [3,2,0,-4]
pos = 1
linkedList1 = initialLinkedList_Cycle(valList1, pos)
assert sol.hasCycle_hast(linkedList1)
assert sol.hasCycle_2pointer(linkedList1)

valList1 = [3,2,0,-4]
pos = -1
linkedList1 = initialLinkedList_Cycle(valList1, pos)
assert not sol.hasCycle_hast(linkedList1)
assert not sol.hasCycle_2pointer(linkedList1)
