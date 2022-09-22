from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxSum(node):
            nonlocal max_sum
            if node is None:
                return 0
            left=maxSum(node.left)
            right=maxSum(node.right)
            leftSum=left+node.val
            rightSum=right+node.val
            leftrightSum=left+right+node.val
            max_sum=max(leftSum,rightSum,leftrightSum,node.val,max_sum)

            return max(node.val,leftSum,rightSum)

        max_sum=float("-inf")
        maxSum(root)
        return max_sum