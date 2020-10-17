# Created by Jiehan Zhu at 10/17/20

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def initialLinkedList(val_list):
    head = ListNode(val_list[0])
    nodePrior = head
    for val in val_list[1:]:
        node = ListNode(val, None)
        nodePrior.next = node
        nodePrior = node
    return head


def initialLinkedList_Cycle(val_list, pos):
    head = ListNode(val_list[0])
    nodeprior = head
    for val in val_list[1:]:
        node = ListNode(val)
        nodeprior.next = node
        nodeprior = node

    if pos == -1:
        return head

    tail = node
    node = head
    for _ in range(pos-1):
        node = node.next
    tail.next = node
    return head


def getLinkedListVal(root: ListNode):
    valls = []
    node = root
    while node:
        valls.append(node.val)
        node = node.next
    return valls
