from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q=[]
        q.append(root)
        while q:
            node=q.pop(0)
            if node.left and node.right:
                q.append(node.right)
                q.append(node.left)
                node.left,node.right=node.right,node.left
            elif node.left and not node.right:
                q.append(node.left)
                node.left,node.right=None,node.left
            elif node.right and not node.left:
                q.append(node.right)
                node.left,node.right=node.right,None
        return root