"""
Utility functions for Advent of Code solutions.

Start simple and add functions as you learn and need them!
"""

# Import essential file I/O functions
from .file_io import (
    read_input,
    read_lines,
    read_integers,
)

# Make functions available at package level
__all__ = [
    "read_input",
    "read_lines", 
    "read_integers",
]