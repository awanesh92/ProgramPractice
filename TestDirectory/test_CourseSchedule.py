import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from Graph.CourseSchedule import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("numCourses, prerequisites, expected", [
        (2, [[1,0]], True),
        (2, [[1,0],[0,1]], False)
    ])
    def test_sumOfSubarrayMins(self, solution, numCourses, prerequisites, expected):
        result=solution.canFinish(numCourses, prerequisites)
        assert result == expected