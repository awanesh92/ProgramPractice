from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=[]
        res=[]
        q.append(root)
        while q:
            temp=[]
            s,l=0,len(q)
            while q:
                tnode=q.pop()
                s+=tnode.val
                if tnode.left:
                    temp.append(tnode.left)
                if tnode.right:
                    temp.append(tnode.right)
            res.append(s/l)
            while temp:
                q.append(temp.pop())
        return res