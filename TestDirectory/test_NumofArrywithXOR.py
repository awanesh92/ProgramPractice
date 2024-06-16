import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from NumofArrywithXOR import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("a, k, expected", [
        ([4, 2, 2, 6, 4], 6,4),
        ([5, 6, 7, 8, 9],5,2 )
    ])
    def test_countOfArryXOR(self, solution, a, k, expected):
        result=solution.solve(a,k)
        assert result == expected