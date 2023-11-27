import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from CompareVersion import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("v1, v2, expected", [
        ("1.01","1.001",0),
        ("1.0.3","1.0.0",1),
        ("0.1","1.1",-1),
        ("7.5.2.4","7.5.3",-1)
    ])
    def test_countAndSay(self, solution, v1, v2, expected):
        result=solution.compareVersion(v1,v2)
        assert result == expected