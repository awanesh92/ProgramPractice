import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from FindMissingRepeatingnum import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("arr, n, expected", [
        ([2,2],2, [2,1]),
        ([1,3,3],3,[3,2])
    ])
    def test_countOfArryXOR(self, solution, arr, n, expected):
        result=solution.findTwoElement(arr,n)
        assert result == expected