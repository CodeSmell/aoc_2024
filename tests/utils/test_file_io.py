"""
Tests for file I/O utility functions.
"""

import pytest
import tempfile
import os
from pathlib import Path
from aoc2024.utils.file_io import (
    read_input,
    read_lines,
    read_integers,
)

# reusable set up code
@pytest.fixture
def generate_temp_file(tmp_path):
    def _create_temp_file(content: str):
        file = tmp_path / "temp.txt"
        file.write_text(content)
        return str(file)
    return _create_temp_file

class TestFileIO:
    def test_read_input_string_path(self, generate_temp_file):
        temp_file_path = generate_temp_file("Hello World\n  \n")
        result = read_input(temp_file_path)
        assert result == "Hello World"

    def test_read_lines(self, generate_temp_file):
        temp_file_path = generate_temp_file("Line 1\nLine 2  \n  Line 3\n")
        result = read_lines(temp_file_path)
        assert result == ["Line 1", "Line 2", "Line 3"]

    def test_read_integers(self, generate_temp_file):
        temp_file_path = generate_temp_file("123\n456\n789\n\n")  # Empty line should be skipped
        result = read_integers(temp_file_path)
        assert result == [123, 456, 789]

    def test_empty_file(self, generate_temp_file):
        temp_file_path = generate_temp_file("")
        result = read_input(temp_file_path)
        assert result == ""
        
        lines = read_lines(temp_file_path)
        assert lines == []
        
        integers = read_integers(temp_file_path)
        assert integers == []

    def test_nonexistent_file(self):
        fake_path = "nonexistent_file_12345.txt"
        with pytest.raises(FileNotFoundError):
            read_input(fake_path)
        with pytest.raises(FileNotFoundError):
            read_lines(fake_path)
        with pytest.raises(FileNotFoundError):
            read_integers(fake_path)