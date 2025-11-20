import pytest
from aoc2024.day04.day04 import part_one, part_two

class TestDay04:
    def test_part_one_sample(self):
        """Test part one with sample data."""
        # TODO: Add expected result when problem is known
        result = part_one("inputs/day04.sample.txt")
        assert isinstance(result, int)
        # assert result == expected_value

    def test_part_one_actual(self):
        """Test part one with actual data."""
        # TODO: Add expected result when problem is solved
        result = part_one("inputs/day04.txt")
        assert isinstance(result, int)
        # assert result == expected_value

    def test_part_two_sample(self):
        """Test part two with sample data."""
        # TODO: Add expected result when problem is known
        result = part_two("inputs/day04.sample.txt")
        assert isinstance(result, int)
        # assert result == expected_value

    def test_part_two_actual(self):
        """Test part two with actual data."""
        # TODO: Add expected result when problem is solved
        result = part_two("inputs/day04.txt")
        assert isinstance(result, int)
        # assert result == expected_value

# Additional test classes can be added here for individual functions
# class TestSpecificFunction:
#     def test_specific_function(self):
#         pass