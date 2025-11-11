"""
Tests for Advent of Code 2024 - Day 1: Historian Hysteria
"""

import pytest
from aoc2024.day01.day01 import (
    distance, read_day01_input
)

class TestDistance:
    """Test cases for the distance function."""

    def test_distance_positive_numbers(self):
        """Test distance calculation with positive numbers."""
        assert distance(3, 7) == 4
        assert distance(7, 3) == 4
        assert distance(9, 3) == 6
        assert distance(3, 9) == 6

    def test_distance_negative_numbers(self):
        """Test distance calculation with negative numbers."""
        assert distance(-3, -7) == 4
        assert distance(-7, -3) == 4
        assert distance(-9, 3) == 12
        assert distance(3, -9) == 12

    def test_distance_with_zero(self):
        """Test distance calculation involving zero."""
        assert distance(0, 5) == 5
        assert distance(5, 0) == 5
        assert distance(0, -5) == 5
        assert distance(-5, 0) == 5
        assert distance(0, 0) == 0

    def test_distance_same_numbers(self):
        """Test distance when both numbers are the same."""
        assert distance(5, 5) == 0
        assert distance(-3, -3) == 0
        assert distance(100, 100) == 0

    def test_distance_floating_point(self):
        """Test distance calculation with floating point numbers."""
        assert distance(3.5, 7.2) == 3.7
        assert distance(1.1, 1.4) == pytest.approx(0.3)
        assert distance(-2.5, 1.5) == 4.0

    def test_distance_large_numbers(self):
        """Test distance calculation with large numbers."""
        assert distance(1000000, 2000000) == 1000000
        assert distance(-1000000, 1000000) == 2000000

class TestReadDay01Input:
    """Test cases for the read_day01_input function."""

    def test_read_day01_input_valid_file(self, tmp_path):
        left, right = read_day01_input("inputs/day01.sample.txt")

        assert left == [3, 4, 2, 1, 3, 3]
        assert right == [4, 3, 5, 3, 9, 3]

    def test_read_day01_input_empty_file(self, tmp_path):
        """Test reading an empty file."""
        test_file = tmp_path / "test_input.txt"
        test_file.write_text("")

        left, right = read_day01_input(str(test_file))

        assert left == []
        assert right == []

    def test_read_day01_input_single_line(self, tmp_path):
        """Test reading a file with a single line."""
        test_file = tmp_path / "test_input.txt"
        test_file.write_text("42   24\n")

        left, right = read_day01_input(str(test_file))

        assert left == [42]
        assert right == [24]

    def test_read_day01_input_skips_invalid_lines(self, tmp_path):
        """Test that lines without exactly two numbers are skipped."""
        test_file = tmp_path / "test_input.txt"
        test_file.write_text("3   4\n1\n2   5   6\n7   8\n")

        left, right = read_day01_input(str(test_file))

        assert left == [3, 7]
        assert right == [4, 8]


# Example of how to add more test classes for other functions
# class TestPartOne:
#     """Test cases for part_one function."""
#     pass
#
# class TestPartTwo:
#     """Test cases for part_two function."""
#     pass
