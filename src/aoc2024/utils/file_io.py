"""
File reading utilities for Advent of Code solutions.

This module provides simple functions for reading and parsing input files.
Keep it simple - add more functions as you need them!
"""

from pathlib import Path
from typing import List, Union


def read_input(filename: Union[str, Path]) -> str:
    """
    Read a file and return its contents as a string.
    
    Args:
        filename: Path to the file to read
        
    Returns:
        File contents as a string with trailing whitespace stripped
        
    Example:
        content = read_input("inputs/day01.txt")
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().strip()


def read_lines(filename: Union[str, Path]) -> List[str]:
    """
    Read a file and return its contents as a list of lines.
    
    Args:
        filename: Path to the file to read
        
    Returns:
        List of lines with trailing whitespace stripped from each line
        
    Example:
        lines = read_lines("inputs/day01.txt")
        for line in lines:
            print(line)
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]


def read_integers(filename: Union[str, Path]) -> List[int]:
    """
    Read a file and return its contents as a list of integers.
    
    Each line should contain one integer. Empty lines are skipped.
    
    Args:
        filename: Path to the file to read
        
    Returns:
        List of integers
        
    Example:
        numbers = read_integers("inputs/day01.txt")
    """
    lines = read_lines(filename)
    return [int(line) for line in lines if line.strip()]