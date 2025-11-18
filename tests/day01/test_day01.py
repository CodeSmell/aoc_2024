import pytest
from aoc2024.day01.day01 import (
    distance, similarity, read_day01_input, pair_and_sum_distances, part_one, part_two
)

class TestDistance:
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


class TestPairAndSumDistances:
    def test_pair_and_sum_distances_basic(self):
        """Test basic pairing and sum of distances."""
        left = [3, 4, 2, 1, 3, 3]
        right = [4, 3, 5, 3, 9, 3]

        result = pair_and_sum_distances(left, right)

        assert result == 11

    def test_pair_and_sum_distances_empty_lists(self):
        """Test with empty lists."""
        left = []
        right = []

        result = pair_and_sum_distances(left, right)

        assert result == 0

    def test_pair_and_sum_distances_single_element(self):
        """Test with single element lists."""
        left = [5]
        right = [8]

        result = pair_and_sum_distances(left, right)

        assert result == 3

    def test_pair_and_sum_distances_already_sorted(self):
        """Test with already sorted lists."""
        left = [1, 2, 3]
        right = [4, 5, 6]

        result = pair_and_sum_distances(left, right)

        assert result == 9

    def test_pair_and_sum_distances_reverse_sorted(self):
        """Test with reverse sorted lists."""
        left = [6, 5, 4]
        right = [3, 2, 1]

        result = pair_and_sum_distances(left, right)

        assert result == 9

class TestSimilarity:
    def test_similarity_basic_example(self):
        left = [3, 4, 2, 1, 3, 3]
        right = [4, 3, 5, 3, 9, 3]

        result = similarity(left, right)

        assert result == 31

    def test_similarity_empty_lists(self):
        left = []
        right = []

        result = similarity(left, right)

        assert result == 0

    def test_similarity_no_matches(self):
        left = [1, 2, 3]
        right = [4, 5, 6]

        result = similarity(left, right)

        assert result == 0

    def test_similarity_all_matches(self):
        left = [1, 2, 3]
        right = [1, 2, 3]

        result = similarity(left, right)

        assert result == 6

    def test_similarity_zero_in_lists(self):
        left = [0, 1, 2]
        right = [0, 0, 1]

        result = similarity(left, right)

        assert result == 1  # 0*2 + 1*1 + 2*0

class TestPartOne:
    def test_part_one_sample_file(self):
        left_numbers, right_numbers = read_day01_input("inputs/day01.sample.txt")
        result = part_one(left_numbers, right_numbers)

        assert result == 11

    def test_part_one_empty_file(self, tmp_path):
        test_file = tmp_path / "test_input.txt"
        test_file.write_text("")

        left_numbers, right_numbers = read_day01_input(str(test_file))
        result = part_one(left_numbers, right_numbers)

        assert result == 0

class TestPartTwo:
    def test_part_two_sample_file(self):
        left_numbers, right_numbers = read_day01_input("inputs/day01.sample.txt")
        result = part_two(left_numbers, right_numbers)

        assert result == 31

    def test_part_two_empty_file(self, tmp_path):
        test_file = tmp_path / "test_input.txt"
        test_file.write_text("")

        left_numbers, right_numbers = read_day01_input(str(test_file))
        result = part_two(left_numbers, right_numbers)

        assert result == 0
