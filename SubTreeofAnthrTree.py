from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSameTree(self,p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return p is q

# Helper function to construct a binary tree from a list
def list_to_tree(lst, index):
    if index < len(lst):
        if lst[index] is None:
            return None
        else:
            node = TreeNode(lst[index])
            node.left = list_to_tree(lst, 2 * index + 1)
            node.right = list_to_tree(lst, 2 * index + 2)
            return node
    return None

# Create binary tree nodes from the input lists
root_list = [3, 4, 5, 1, 2]
subRoot_list = [4, 1, 2]

root = list_to_tree(root_list, 0)
subRoot = list_to_tree(subRoot_list, 0)

# Create a Solution object
solution = Solution()

# Call the isSubtree method and assert the result
assert solution.isSubtree(root, subRoot) == True