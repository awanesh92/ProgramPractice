from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result=[]
        temp = []
        def dfs(node, temp):
            if not node:
                return ''

            if not node.left and not node.right:
                temp.append(chr(node.val + 97))
                result.append(''.join(temp)[::-1])
                return
            temp.append(chr(node.val + 97))
            dfs(node.left, temp.copy())
            dfs(node.right, temp.copy())

        dfs(root, temp)
        return min(result)