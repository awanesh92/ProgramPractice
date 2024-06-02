import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from DeepestLeavesSum import Solution, TreeNode
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_deepestLeavesSum(self,solution):
        # Create a binary tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        root.left.left.left = TreeNode(7)
        root.right.right.right = TreeNode(8)

        # Test case 1: Test the sum of the deepest leaves
        assert solution.deepestLeavesSum(root) == 15

        # Test case 2: Test with an empty tree
        root = None
        assert solution.deepestLeavesSum(root) == 0

        # Test case 3: Test with a tree with a single node
        root = TreeNode(1)
        assert solution.deepestLeavesSum(root) == 1