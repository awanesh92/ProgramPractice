import pytest

from RemoveNodesFromLinkList import Solution, ListNode
class TestRemoveNodes():
    # Helper function to create a linked list from a list of values
    def create_linked_list(self,values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert a linked list into a list
    def linked_list_to_list(self,head):
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    # Test cases
    @pytest.mark.parametrize("input_list,expected_output", [
        ([1, 2, 3, 4, 5], [5]),
        ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
        ([1, 2, 3, 2, 1], [3, 2, 1]),
        ([], []),
    ])
    def test_removeNodes(self,input_list, expected_output):
        # Create a linked list from input list
        input_head = self.create_linked_list(input_list)

        # Apply the function
        solution = Solution()
        result_head = solution.removeNodes(input_head)

        # Convert the result back to list for comparison
        result_list = self.linked_list_to_list(result_head)

        # Assert the result
        assert result_list == expected_output