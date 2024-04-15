import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from SumOfLeftLeaves import Solution, TreeNode
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    def example_tree():
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        return root
    @pytest.mark.parametrize("root, expected", [
        (example_tree(), 24)
    ])
    def test_removeKDigits(self, solution, root, expected):
        result = solution.sumOfLeftLeaves(root)
        assert result == expected