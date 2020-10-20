# Created by Jiehan Zhu at 10/16/20
"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
from src.main.python.utility.tree import TreeNode, initial_tree


class Solution:
    def isValidBST1(self, root: TreeNode) -> bool:
        """
        Only look at immediate children. This does not check the relationship between root and its grandchildren.
        for example, [10, 5, 3, 6, 15, 7, 20] is not a valid Search Tree, but this method would not catch it.
        :param root:
        :return:
        """
        print(f'root = {root}')
        if not root or (not root.left and not root.right):
            return True
        if not root.left:
            if root.right.val <= root.val:
                return False
            else:
                return self.isValidBST(root.right)
        if not root.right:
            if root.left.val >= root.val:
                return False
            else:
                return self.isValidBST(root.left)
        if root.left.val >= root.val or root.right.val <= root.val:
            return False
        return all([self.isValidBST(root.left), self.isValidBST(root.right)])

    def isValidBST2(self, root: TreeNode) -> bool:
        """
        first solution.

        Runtime: 44 ms. Your runtime beats 74.50 % of python3 submissions.
        Memory Usage: 16.4 MB
        :param root:
        :return:
        """
        def getRange(root, rootRange):
            minVal, maxVal = rootRange
            left_range = (minVal, root.val)
            right_range = (root.val, maxVal)
            return left_range, right_range

        def checkRange(node, rangeVal):
            if rangeVal[0] is not None and node.val <= rangeVal[0]:
                return False
            if rangeVal[1] is not None and node.val >= rangeVal[1]:
                return False
            return True

        def ValidTree(root: TreeNode, root_range):
            if not root:
                return True
            # print(f'root = {root.val, root.left, root.left}')
            left_range, right_range = getRange(root, root_range)
            if not root.right and not root.left:
                return True
            result = True
            if root.right and checkRange(root.right, right_range):
                result = result and ValidTree(root.right, right_range)
            elif root.right:
                return False
            if root.left and checkRange(root.left, left_range):
                result = result and ValidTree(root.left, left_range)
            elif root.left:
                return False
            return result

        return ValidTree(root, (None, None))

    def isValidBST3(self, root: TreeNode) -> bool:
        """
        simplify the solution

        :param root:
        :return:
        """
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            if node.val <= lower or node.val >= upper:
                return False
            stack.append((node.right, node.val, upper))
            stack.append((node.left, lower, node.val))
        return True


sol = Solution()

root = initial_tree([10, 5, 15, 3, 6, 12, 20])
assert sol.isValidBST2(root)
root = initial_tree([10, 5, 15, 3, 6, 12, 20])
assert sol.isValidBST3(root)

root = initial_tree([5, 1, 6, None, None, 3, 7])
assert not sol.isValidBST2(root)
root = initial_tree([5, 1, 6, None, None, 3, 7])
assert not sol.isValidBST3(root)

root = initial_tree([0, None, -1])
assert not sol.isValidBST2(root)
root = initial_tree([0, None, -1])
assert not sol.isValidBST3(root)
