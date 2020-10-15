"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/

Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.
Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome_reverseLinkedlist(self, head: ListNode) -> bool:
        """
        Brute force, reverse the linked list

        Runtime: 108 ms. Your runtime beats 15.36 % of python3 submissions.
        Memory Usage: 31.6 MB
        """
        if not head:
            return True
        # print(f'head = {head}')
        reverseHead = ListNode(head.val, None)
        node = head.next
        while node:
            reverseHead = ListNode(node.val, reverseHead)
            node = node.next
        # print(f'reverseHead = {reverseHead}')
        node = head
        node2 = reverseHead
        while node and node2:
            # print(f'node, node2 = {node, node2}')
            if node.val != node2.val:
                return False
            node = node.next
            node2 = node2.next
        return True

    def isPalindrome_List(self, head: ListNode) -> bool:
        """
        Brute force change linked list to a stack list

        Runtime: 64 ms. Your runtime beats 94.24 % of python3 submissions.
        Memory Usage: 24.3 MB
        """
        if not head:
            return True
        # print(f'head = {head}')
        stack = []
        node = head
        while node:
            stack .append(node.val)
            node = node.next
        # print(f'valList = {valList}')
        return stack == stack[::-1]
        # for i in range(int(len(stack) / 2)):
        #     if stack[i] != stack[-(i+1)]:
        #         return False
        # return True


# Tests
def initialLinkedList(val_list):
    head = ListNode(val_list[0])
    nodePrior = head
    for val in val_list[1:]:
        node = ListNode(val, None)
        nodePrior.next = node
        nodePrior = node
    return head

sol = Solution()
valList1 = [1, 2, 2, 1]
linkedList1 = initialLinkedList(valList1)
assert sol.isPalindrome_List(linkedList1)


valList2 = [1, 2, 3, 1]
linkedList2 = initialLinkedList(valList2)
assert not sol.isPalindrome_List(linkedList2)
