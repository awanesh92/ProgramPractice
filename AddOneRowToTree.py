from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node


        q = deque([(root, 1)])

        while q:
            node, curr_depth = q.popleft()

            if curr_depth == depth - 1:
                left_child = TreeNode(val)
                right_child = TreeNode(val)
                left_child.left = node.left
                right_child.right = node.right
                node.left = left_child
                node.right = right_child

            if node.left:
                q.append((node.left, curr_depth + 1))
            if node.right:
                q.append((node.right, curr_depth + 1))

        return root