# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        lastNode=prev=startNode=None

        def dfs(node):
            nonlocal lastNode,prev,startNode
            if not node:
                return None

            dfs(node.left)

            if prev and prev.val>node.val:
                if not startNode:
                    startNode=node
                lastNode=prev

            prev=node

            dfs(node.right)

        dfs(root)

        if lastNode and startNode:
            startNode.val,lastNode.val=lastNode.val,startNode.val