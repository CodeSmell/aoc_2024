import pytest
from aoc2024.day02.day02 import (
    is_safe_range, is_safe_report, is_safe_report_toleration, part_one, part_two
)

day2_test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

class TestIsSafeRange:
    def test_safe_range_within_limit(self):
        assert is_safe_range(5, 7) is True
        assert is_safe_range(10, 13) is True
        assert is_safe_range(0, 3) is True

    def test_safe_range_at_boundary(self):
        assert is_safe_range(3, 0) is True
        assert is_safe_range(0, 3) is True
        assert is_safe_range(-3, 0) is True

    def test_safe_range_outside_limit(self):
        assert is_safe_range(1, 5) is False
        assert is_safe_range(10, 20) is False
        assert is_safe_range(-4, 0) is False

    def test_safe_range_with_negatives_and_zero(self):
        assert is_safe_range(-2, 1) is True
        assert is_safe_range(-3, -6) is True
        assert is_safe_range(-3, -7) is False

    def test_same_value(self):
        assert is_safe_range(4,4) is False
        assert is_safe_range(0, 0) is False        
        assert is_safe_range(-5, -5) is False  

class TestIsSafeReport:
    def test_trivial_safe_empty(self):
        assert is_safe_report([]) is True

    def test_trivial_safe_single(self):
        assert is_safe_report([5]) is True

    def test_all_increasing_within_range(self):
        report = [1,3,6,7,9]
        assert is_safe_report(report) is True

    def test_all_decreasing_within_range(self):
        report = [7,6,4,2,1]
        assert is_safe_report(report) is True

    def test_increasing_not_within_range(self):
        report = [1,2,7,8,9]
        assert is_safe_report(report) is False

    def test_decreasing_not_within_range(self):
        report = [9,7,6,2,1]
        assert is_safe_report(report) is False

    def test_equal_levels(self):
        assert is_safe_report([2, 2, 2]) is False
        assert is_safe_report([5, 5]) is False

    def test_negative_levels_increasing(self):
        assert is_safe_report([-5, -3, -1]) is True

    def test_negative_levels_decreasing(self):
        assert is_safe_report([-1, -3, -5]) is True

    def test_mixed_signs_increasing(self):
        assert is_safe_report([-2, 0, 2]) is True

    def test_mixed_signs_decreasing(self):
        assert is_safe_report([2, 0, -2]) is True

    def test_pair_not_safe(self):
        assert is_safe_report([1, 5]) is False
        assert is_safe_report([5, 1]) is False

class TestIsSafeReportToleration:
    def test_trivial_safe_empty(self):
        assert is_safe_report_toleration([]) is True

    def test_trivial_safe_single(self):
        assert is_safe_report_toleration([5]) is True

    def test_all_increasing_within_range(self):
        report = [1,3,6,7,9]
        assert is_safe_report_toleration(report) is True

    def test_all_decreasing_within_range(self):
        report = [7,6,4,2,1]
        assert is_safe_report_toleration(report) is True

    def test_increasing_not_within_range(self):
        report = [1,2,7,8,9]
        assert is_safe_report_toleration(report) is False

    def test_decreasing_not_within_range(self):
        report = [9,7,6,2,1]
        assert is_safe_report_toleration(report) is False

    def test_increasing_tolerated(self):
        report = [1,3,2,4,5]
        assert is_safe_report_toleration(report) is True

    def test_decreasing_tolerated(self):
        report = [8,6,4,4,1]
        assert is_safe_report_toleration(report) is True

    def test_all_increasing_within_range_fakeout(self):
        report = [4,1,3,6,7,9]
        assert is_safe_report_toleration(report) is True

    def test_decreasing_tolerated_fakeout(self):
        report = [2,7,6,4,2,1]
        assert is_safe_report_toleration(report) is True

    def test_equal_levels(self):
        assert is_safe_report_toleration([2, 2, 2]) is False
        assert is_safe_report_toleration([5, 5]) is True

    def test_negative_levels_increasing(self):
        assert is_safe_report_toleration([-5, -3, -1]) is True

    def test_negative_levels_decreasing(self):
        assert is_safe_report_toleration([-1, -3, -5]) is True

    def test_mixed_signs_increasing(self):
        assert is_safe_report_toleration([-2, 0, 2]) is True

    def test_mixed_signs_decreasing(self):
        assert is_safe_report_toleration([2, 0, -2]) is True

    def test_pair_not_safe(self):
        assert is_safe_report_toleration([1, 5]) is True
        assert is_safe_report_toleration([5, 1]) is True


class TestPartOne:
    def test_part_one_sample(self):
        reports = day2_test_data.splitlines()
        assert part_one(reports) == 2

class TestPartTwo:
    def test_part_two_sample(self):
        reports = day2_test_data.splitlines()
        assert part_two(reports) == 4