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


class TestFileIO:
    """Test cases for file I/O utility functions."""

    def test_read_input_string_path(self):
        """Test reading input with string path."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("Hello World\n  \n")
            temp_path = f.name
        
        try:
            result = read_input(temp_path)
            assert result == "Hello World"
        finally:
            os.unlink(temp_path)

    def test_read_input_path_object(self):
        """Test reading input with Path object."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("Hello World\n  \n")
            temp_path = Path(f.name)
        
        try:
            result = read_input(temp_path)
            assert result == "Hello World"
        finally:
            temp_path.unlink()

    def test_read_lines(self):
        """Test reading lines from file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("Line 1\nLine 2  \n  Line 3\n")
            temp_path = f.name
        
        try:
            result = read_lines(temp_path)
            assert result == ["Line 1", "Line 2", "Line 3"]
        finally:
            os.unlink(temp_path)

    def test_read_integers(self):
        """Test reading integers from file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("123\n456\n789\n\n")  # Empty line should be skipped
            temp_path = f.name
        
        try:
            result = read_integers(temp_path)
            assert result == [123, 456, 789]
        finally:
            os.unlink(temp_path)

    def test_empty_file(self):
        """Test handling of empty files."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name
        
        try:
            result = read_input(temp_path)
            assert result == ""
            
            lines = read_lines(temp_path)
            assert lines == []
            
            integers = read_integers(temp_path)
            assert integers == []
        finally:
            os.unlink(temp_path)