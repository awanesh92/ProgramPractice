import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from BoatsToSavePeople import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("people, limit, expected", [
        ([3,5,3,4], 5, 4),
        ([1,2], 3, 1),
        ([3,2,2,1], 3, 3)
    ])
    def test_countAndSay(self, solution, people, limit, expected):
        result=solution.numRescueBoats(people,limit)
        assert result == expected