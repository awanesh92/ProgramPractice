import sys
import os
current_file_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(current_file_directory, ".."))

sys.path.append(parent_directory)

from Graph.CourseScheduleII import Solution
import pytest

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    @pytest.mark.parametrize("numCourses, prerequisites, expected", [
        (2, [[1,0]], [0,1]),
        (4, [[1,0],[2,0],[3,1],[3,2]], [0,1,2,3])
    ])
    def test_sumOfSubarrayMins(self, solution, numCourses, prerequisites,expected):
        result=solution.findOrder(numCourses, prerequisites)
        assert result == expected