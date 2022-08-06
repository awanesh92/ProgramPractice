from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    res = []

    def dfsHelper(self, root, tsum, path):
        if root == None:
            return
        tsum -= root.val
        path.append(root.val)
        if root.left == None and root.right == None:
            if tsum == 0:
                Solution.res.append(path[:])
                path.pop()
                return
        self.dfsHelper(root.left, tsum, path)
        self.dfsHelper(root.right, tsum, path)
        path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.dfsHelper(root, targetSum, [])
        return Solution.res