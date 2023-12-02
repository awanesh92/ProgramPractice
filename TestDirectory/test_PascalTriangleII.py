import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from PascaltriangleII import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("rowIndex, expected",[
        (3,[1,3,3,1]),
         (0,[1]),
         (1,[1,1])
    ])
    def test_findPairs(self, solution, rowIndex, expected):
        result=solution.getRow(rowIndex)
        assert result == expected