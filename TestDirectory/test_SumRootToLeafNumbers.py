import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from SumRootToLeafNumbers import Solution, TreeNode
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    def example_tree():
        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)
        return root
    @pytest.mark.parametrize("root, expected", [
        (example_tree(), 1026)
    ])
    def test_sumRootLeafNumbers(self, solution, root, expected):
        result = solution.sumNumbers(root)
        assert result == expected