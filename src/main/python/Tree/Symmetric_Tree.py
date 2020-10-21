# Created by Jiehan Zhu at 10/17/20
"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/

Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
But the following [1,2,2,null,3,null,3] is not:

Follow up: Solve it both recursively and iteratively.
"""
from src.main.python.utility.tree import TreeNode, initial_tree


class Solution:
    def isSymmetric_iteractive(self, root: TreeNode) -> bool:
        """
        interactively with stack

        Runtime: 40 ms. Your runtime beats 27.24 % of python3 submissions.
        Memory Usage: 14.3 MB
        :param root:
        :return:
        """
        if not root:
            return True
        layer = [root.left, root.right]
        while layer:
            nextlayer = []
            while layer:
                node1 = layer.pop(0)
                node2 = layer.pop(-1)
                if not node1 and not node2:
                    continue
                elif not node1 or not node2:
                    return False
                if node1.val != node2.val:
                    return False
                nextlayer.insert(0, node1.right)
                nextlayer.insert(0, node1.left)
                nextlayer.append(node2.left)
                nextlayer.append(node2.right)
            layer = nextlayer
        return True

    def isSymmetric_recursive(self, root: TreeNode) -> bool:
        """
        recursively

        Runtime: 48 ms. Your runtime beats 16.23 % of python3 submissions.
        Memory Usage: 14.3 MB
        :param root:
        :return:
        """
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return root1.val == root2.val and self.check(root1.left, root2.right) and self.check(root1.right, root2.left)


sol = Solution()

root = initial_tree([1,2,2,3,4,4,3])
assert sol.isSymmetric_iteractive(root)
assert sol.isSymmetric_recursive(root)

root = initial_tree([1,2,2,None,4,4,None])
assert sol.isSymmetric_iteractive(root)
assert sol.isSymmetric_recursive(root)
