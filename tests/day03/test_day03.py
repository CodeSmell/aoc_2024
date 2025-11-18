import pytest
from aoc2024.day03.day03 import find_good_commands, run_good_commands


class Test_FindGoodCommands:
    def test_find_good_commands_basic(self):
        s = "mul(2,4) and mul(5,5) and mul(11,8) and mul(8,5)"
        expected = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
        assert find_good_commands(s) == expected

    def test_find_good_commands_with_noise(self):
        s = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        expected = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
        assert find_good_commands(s) == expected

    def test_find_good_commands_with_conditions(self):
        s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        expected = ["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"]
        assert find_good_commands(s) == expected
 
    def test_find_good_commands_empty(self):
        s = "no commands here"
        assert find_good_commands(s) == []

    def test_find_good_commands_large_numbers(self):
        s = "mul(123,456) mul(1234,56) mul(1,2)"
        expected = ["mul(123,456)", "mul(1,2)"]
        assert find_good_commands(s) == expected


class Test_RunGoodCommands:
    def test_run_good_commands_empty_off(self):
        commands = []
        assert run_good_commands(commands, False) == 0

    def test_run_good_commands_empty_on(self):
        commands = []
        assert run_good_commands(commands, True) == 0

    def test_run_good_commands_bad(self):
        commands = ["mul(2,4)", "nop(5,5)", "mul(11,8)", "mul(8,5)"]
        assert run_good_commands(commands, False) == 136

    def test_run_good_commands_basic_off(self):
        commands = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
        assert run_good_commands(commands, False) == 161

    def test_run_good_commands_basic_on(self):
        commands = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
        assert run_good_commands(commands, True) == 161

    def test_run_good_commands_conditional(self):
        commands = ["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"]
        assert run_good_commands(commands, True) == 48

    def test_run_good_commands_conditional_multi(self):
        commands = ["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)", "don't()", "mul(5,5)", "do()", "mul(3,3)"]
        assert run_good_commands(commands, True) == 57