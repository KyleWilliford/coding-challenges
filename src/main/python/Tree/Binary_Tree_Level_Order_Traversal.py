"""
Created by Jiehan Zhu at 10/17/20

https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/

Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""
from src.main.python.utility.tree import TreeNode, initial_tree
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Runtime: 32 ms. Your runtime beats 83.92 % of python3 submissions.
        Memory Usage: 14.2 MB
        :param root:
        :return:
        """
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            _ = []
            result.append([])
            for node in stack:
                if node is None:
                    continue
                result[-1].append(node.val)
                if node.left is not None:
                    _.append(node.left)
                if node.right is not None:
                    _.append(node.right)
            stack = _
        return result


sol = Solution()

root = initial_tree([1,2,2,3,4,4,3])
assert sol.levelOrder(root) == [[1], [2, 2], [3, 4, 4, 3]]

root = initial_tree([1,2,2,None,4,4,None])
assert sol.levelOrder(root) == [[1], [2, 2], [4, 4]]
