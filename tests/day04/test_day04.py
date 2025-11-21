import pytest
from aoc2024.day04.day04 import (
    count_word_in_line, search_lines, 
    get_columns, get_diagonals,
    part_one, part_two
)

day04_test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


class TestCountWordInLine:
    def test_count_word_in_line_single_match(self):
        line = "XMASXXXXXX"
        assert count_word_in_line(line, "XMAS") == 1

    def test_count_word_in_line_single_reversed(self):
        line = "SAMXXXXXXX"
        assert count_word_in_line(line, "XMAS") == 1

    def test_count_word_in_line_multiple_matches(self):
        line = "XMASXMASXMAS"
        assert count_word_in_line(line, "XMAS") == 3

    def test_count_word_in_line_multiple_matches_reversed(self):
        line = "SAMXSAMXSAMX"
        assert count_word_in_line(line, "XMAS") == 3

    def test_count_word_in_line_mixed_forward_backward(self):
        line = "XMASSAMX"
        assert count_word_in_line(line, "XMAS") == 2

    def test_count_word_in_line_overlapping(self):
        line = "XMASAMX"
        assert count_word_in_line(line, "XMAS") == 2

    def test_count_word_in_line_no_match(self):
        line = "ABCDEFGH"
        assert count_word_in_line(line, "XMAS") == 0

    def test_count_word_in_line_exact_length(self):
        line = "XMAS"
        assert count_word_in_line(line, "XMAS") == 1

    def test_count_word_in_line_exact_length_reversed(self):
        line = "SAMX"
        assert count_word_in_line(line, "XMAS") == 1

    def test_count_word_in_line_shorter_than_word(self):
        line = "XMA"
        assert count_word_in_line(line, "XMAS") == 0

    def test_count_word_in_line_empty(self):
        line = ""
        assert count_word_in_line(line, "XMAS") == 0


class TestSearchLines:
    def test_search_lines_horizontal(self):
        lines = [
            "XMASXXXXXX",
            "XXXXXXXSAM",
        ]
        assert search_lines(lines, "XMAS") == 1

    def test_search_lines_reversed(self):
        lines = [
            "SAMXXXXXXX",
            "XXXXXXXSAM",
        ]
        assert search_lines(lines, "XMAS") == 1

    def test_search_lines_multiple(self):
        lines = [
            "XMASXMASXMAS",
            "SAMXSAMXSAMX",
        ]
        assert search_lines(lines, "XMAS") == 6

    def test_search_lines_none(self):
        lines = [
            "XXXXXXXXXX",
            "MMMMMMMMMM",
        ]
        assert search_lines(lines, "XMAS") == 0

    def test_search_lines_empty(self):
        lines = []
        assert search_lines(lines, "XMAS") == 0


class TestSampleData:
    def test_foo_grid(self):
        rows = [
            "FOOO",
            "OOOF",
            "OFOF"
        ]
        expected_columns = ["FOO", "OOF", "OOO", "OFF"]
        columns = get_columns(rows)
        assert columns == expected_columns

        expected_diagonals = ['FOO', 'OF', 'O', 'OOF', 'OF', 'O', 'OOF', 'FO', 'F', 'OOO', 'OO', 'F']
        diagonals = get_diagonals(rows)
        assert diagonals == expected_diagonals

        assert search_lines(rows, "FOO") == 2
        assert search_lines(columns, "FOO") == 2
        assert search_lines(diagonals, "FOO") == 3

    def test_get_rows_test_data(self):
        rows = day04_test_data.splitlines()
        assert(search_lines(rows, "XMAS")) == 5

    def test_get_columns_test_data(self):
        rows = day04_test_data.splitlines()
        columns = get_columns(rows)
        assert(search_lines(columns, "XMAS")) == 3

    def test_get_diagonals_test_data(self):
        rows = day04_test_data.splitlines()
        diagonals = get_diagonals(rows)
        assert search_lines(diagonals, "XMAS") == 10

class TestGetColumns:
    def test_get_columns_square_grid(self):
        rows = [
            "ABC",
            "DEF",
            "GHI"
        ]
        expected = ["ADG", "BEH", "CFI"]
        assert get_columns(rows) == expected

    def test_get_columns_rectangular_grid(self):
        rows = [
            "ABCD",
            "EFGH",
            "IJKL",
            "MNOP",
            "QRST"
        ]
        expected = ["AEIMQ", "BFJNR", "CGKOS", "DHLPT"]
        assert get_columns(rows) == expected

    def test_get_columns_single_row(self):
        rows = ["ABCD"]
        expected = ["A", "B", "C", "D"]
        assert get_columns(rows) == expected

    def test_get_columns_single_column(self):
        rows = ["A", 
                "B", 
                "C", 
                "D"
        ]
        expected = ["ABCD"]
        assert get_columns(rows) == expected

    def test_get_columns_test_data(self):
        rows = day04_test_data.splitlines()
        columns = get_columns(rows)
        assert len(columns) == 10  # Should have 10 columns
        assert columns[0] == "MMAMXXSSMM"  # First column
        assert columns[9] == "MAMXMASAMX"  # Last column

    def test_get_columns_empty_rows(self):
        rows = []
        result = get_columns(rows)
        assert result == []

class TestGetDiagonals:
    def test_get_diagonals_square_grid(self):
        rows = [
            "ABC",
            "DEF",
            "GHI"
        ]
        expected = ['AEI', 'DH', 'G', 'BF', 'C', 'CEG', 'FH', 'I', 'BD', 'A']
        assert get_diagonals(rows) == expected

    def test_get_diagonals_rectangular_grid(self):
        rows = [
            "ABCD",
            "EFGH",
            "IJKL",
            "MNOP",
            "QRST"
        ]
        expected = ['AFKP', 'EJOT', 'INS', 'MR', 'Q', 'BGL', 'CH', 'D', 'DGJM', 'HKNQ', 'LOR', 'PS', 'T', 'CFI', 'BE', 'A']
        assert get_diagonals(rows) == expected

    def test_get_diagonals_single_row(self):
        rows = ["ABCD"]
        expected = ['A', 'B', 'C', 'D', 'D', 'C', 'B', 'A']
        print(get_diagonals(rows))
        assert get_diagonals(rows) == expected

    def test_get_diagonals_single_column(self):
        rows = ["A", 
                "B", 
                "C", 
                "D"
        ]
        expected = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
        assert get_diagonals(rows) == expected


    def test_get_diagonals_empty_rows(self):
        rows = []
        result = get_diagonals(rows)
        assert result == []
