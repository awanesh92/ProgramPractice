from typing import Optional
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        lvl=defaultdict(list)
        def dfs(node,level):
            if not node:
                return
            lvl[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)

        dfs(root,0)
        return sum(lvl[len(lvl)-1])