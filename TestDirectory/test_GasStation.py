import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from GasStation import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("gas, cost, expected", [
        ([1,2,3,4,5], [3,4,5,1,2], 3),
        ([2,3,4], [3,4,3], -1),
    ])
    def test_countAndSay(self, solution, gas, cost, expected):
        result=solution.canCompleteCircuit(gas,cost)
        assert result == expected