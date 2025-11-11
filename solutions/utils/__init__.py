"""
Utility functions for Advent of Code solutions.

Start simple and add functions as you learn and need them!
"""

def read_input(filename: str) -> str:
    """
    Read a file and return its contents as a string.
    
    Example:
        content = read_input("day01.txt")
    """
    with open(filename, 'r') as file:
        return file.read().strip()


def read_lines(filename: str) -> list[str]:
    """
    Read a file and return its contents as a list of lines.
    
    Example:
        lines = read_lines("day01.txt")
        for line in lines:
            print(line)
    """
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]