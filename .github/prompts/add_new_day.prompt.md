# Copilot Agent Prompt: Add New Day Boilerplate

mode: 'agent'
model: GPT-4.1
description: 'Setup for another day of puzzles'

---

## Instructions

You are an autonomous coding agent. Your task is to add the necessary folders and boilerplate files for a new day of Advent of Code puzzles in this repository. Follow these steps:

1. **Create a new package** under `src/aoc2024/` named `dayXX` (replace `XX` with the next available day number, e.g., `day10`).
2. **Add an `__init__.py`** file in the new package.
3. **Add a `dayXX.py`** file in the new package, containing:
    - Template functions for `part_one` and `part_two` with docstrings and input reading logic.
    - A `main` block to run both parts with sample and actual input files.
4. **Create a test package** under `tests/dayXX/` with:
    - An `__init__.py` file.
    - A `test_dayXX.py` file with pytest test stubs for both parts, referencing the new module.
5. **Add input files** under `inputs/`:
    - `dayXX.sample.txt` (placeholder/sample input)
    - `dayXX.txt` (placeholder/real input)
6. **Follow naming and structure conventions** used for previous days.
7. **Do not overwrite or modify existing days.**
8. **Output a summary of changes.**

---

## Example Directory Structure

```
src/aoc2024/dayXX/
    __init__.py
    dayXX.py
tests/dayXX/
    __init__.py
    test_dayXX.py
inputs/
    dayXX.sample.txt
    dayXX.txt
```

---

## Example method structure 

def part_one(data: str) -> int:
    pass

def part_two(data: str) -> int:
    pass

if __name__ == "__main__":
    data = read_input("inputs/dayXX.txt")
    print(f"Part 1: {part_one(data)}")
    #print(f"Part 2: {part_two(data)}")
---

## Acceptance Criteria
- All new files and folders are created as described.
- Boilerplate code matches the style of previous days.
- No existing files are modified or deleted.
- A summary of changes is provided at the end.
