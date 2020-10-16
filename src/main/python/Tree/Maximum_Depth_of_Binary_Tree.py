"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth_recursive(self, root: TreeNode) -> int:
        """
        recursive

        Runtime: 40 ms. Your runtime beats 78.70 % of python3 submissions.
        Memory Usage: 15.7 MB
        :param root:
        :return:
        """
        if not root:
            return 0
        return max(self.maxDepth_recursive(root.left), self.maxDepth_recursive(root.right)) + 1

    def maxDepth_stack(self, root: TreeNode) -> int:
        """
        stack
        :param root:
        :return:
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Tests
def initialTree(val_list):
    root = TreeNode(val_list.pop(0))
    currentNodes = [root]
    nextNodes = list()
    i = 0
    while i < len(val_list):
        for node in currentNodes:
            val_left = val_list[i]
            if val_left:
                node.left = TreeNode(val_left)
                nextNodes.append(node.left)
            val_right = val_list[i+1]
            if val_right:
                node.right = TreeNode(val_right)
                nextNodes.append(node.right)
            i += 2
        currentNodes = nextNodes
        nextNodes = list()
    return root


valList = [3,9,20,None,None,15,7]
root = initialTree(valList)

sol = Solution()
assert sol.maxDepth_recursive(root) == 3
