"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
from src.main.python.utility.tree import TreeNode, initialTree


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
valList = [3, 9, 20, None, None, 15, 7]
root = initialTree(valList)

sol = Solution()
assert sol.maxDepth_recursive(root) == 3
