import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from PathIfExistsgraph import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()
    def setup_method(self):
        self.solution = Solution()

    def test_path_exists(self):
        edges = [[0,1],[1,2],[2,0]]
        assert self.solution.validPath(3, edges, 0, 2) is True

    def test_path_does_not_exist(self):
        edges = [[0, 1], [1, 2], [2, 3]]
        assert self.solution.validPath(4, edges, 0, 2) is True

    def test_disconnected_graph(self):
        edges = [[0, 1], [2, 3]]
        assert self.solution.validPath(4, edges, 0, 3) is False