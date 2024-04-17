import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from AddOneRowToTree import Solution, TreeNode
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    def create_tree(self):
        # Create a sample binary tree for testing
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = None
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(1)
        return root

    def test_addOneRow(self, solution):
        root = self.create_tree()
        new_root = solution.addOneRow(root, 1, 3)

        # Assertions for the updated tree structure
        assert new_root.val == 4
        assert new_root.left.val == 2
        assert new_root.right is None
        assert new_root.left.left.val == 1
        assert new_root.left.right.val == 1
        assert new_root.left.left.left.val == 3
        assert new_root.left.left.right is None