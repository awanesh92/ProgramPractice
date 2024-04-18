import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from SmlestStringStartFromLeaf import Solution, TreeNode
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    def construct_tree_from_list(self, lst, index=0):
        if index >= len(lst) or lst[index] is None:
            return None

        root = TreeNode(lst[index])
        root.left = self.construct_tree_from_list(lst, 2 * index + 1)
        root.right = self.construct_tree_from_list(lst, 2 * index + 2)

        return root

    def test_smallestFromLeaf(self, solution):
        root = self.construct_tree_from_list([0,1,2,3,4,3,4])
        result = solution.smallestFromLeaf(root)
        assert 'dba' == result

        root = self.construct_tree_from_list([25,1,3,1,3,0,2])
        result = solution.smallestFromLeaf(root)
        assert 'adz' == result

        root = self.construct_tree_from_list([2,2,1,None,1,0,None,0])
        result = solution.smallestFromLeaf(root)
        assert 'abc' == result