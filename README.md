# 🎄 Advent of Code 2024 - Python Learning Journey

## What is Advent of Code?

[Advent of Code]([adventofcode.com) is an Advent calendar of small programming puzzles for a variety of skill levels

## 🎯 Learning Goals

This particular project isn't just about solving puzzles - it's a comprehensive learning journey focused on:

- **Python Programming**: Building proficiency with Python syntax, data structures, algorithms, and best practices
- **Python Ecosystem**: Exploring libraries, tools, and frameworks that make Python development productive
- **GitHub Copilot**: Learning to effectively collaborate with AI to accelerate development and understanding
- **Problem-Solving Skills**: Breaking down complex problems into manageable pieces

The emphasis is on understanding and learning, not just getting the right answer. Each solution should be well-documented, tested, and serve as a reference for future learning.

## 📁 Project Structure

```
aoc_2024/
├── .vscode/                 # VS Code configuration for Python development
│   └── settings.json        # Python interpreter, linting, formatting settings
├── inputs/                  # Input data files for each day's puzzle
│   └── day01.txt           # Example: Day 1 input data
├── notebooks/              # Jupyter notebooks for exploration and experimentation
│   └── day01_exploration.ipynb  # Interactive problem-solving workspace
├── solutions/              # Python solution modules
│   ├── __init__.py         # Package initialization
│   └── utils/              # Shared utility functions
│       └── __init__.py     # Common file operations, helper functions
├── tests/                  # Test files for solutions
│   └── __init__.py         # Test package initialization
├── venv/                   # Python virtual environment
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.13.9 (or 3.13+) installed on your system
- VS Code (recommended) with Python and Jupyter extensions
- Git for version control

### Setup Instructions

1. **Clone and Navigate to Project**
   ```bash
   cd aoc_2024
   ```

2. **Activate Virtual Environment**
   ```bash
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   If you need to add new packages for solutions:
   ```bash
   pip install package_name
   pip freeze > requirements.txt  # Update requirements file
   ```

4. **Verify Setup**
   ```bash
   # Test that Python can import your solutions
   python -c "from solutions.utils import read_input; print('Setup working!')"
   ```

## 💻 Development Workflow

### For Each Day's Puzzle:

1. **Explore in Jupyter Notebook**
   - Open `notebooks/dayXX_exploration.ipynb`
   - Read and understand the problem
   - Experiment with sample data
   - Prototype solutions interactively

2. **Implement Clean Solution**
   - Create `solutions/dayXX.py`
   - Use utility functions from `solutions/utils/`
   - Write clear, documented code

3. **Write Tests**
   - Create `tests/test_dayXX.py`
   - Test with example data
   - Verify edge cases

4. **Run and Validate**
   ```bash
   # Run specific day's solution
   python solutions/dayXX.py
   
   # Run tests
   pytest tests/test_dayXX.py
   
   # Run all tests
   pytest
   ```

## 🛠️ Development Tools Configured

- **Python Interpreter**: Project virtual environment
- **Linting**: Flake8 for code quality
- **Formatting**: Black for consistent code style
- **Testing**: pytest for unit testing
- **Notebooks**: Jupyter for interactive exploration
- **VS Code**: Optimized settings for Python development

## 📚 Learning Resources

- [Advent of Code Official Site](https://adventofcode.com/)
- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)

## 🤝 Working with GitHub Copilot

This project is designed to be Copilot-friendly:

- **Ask for Explanations**: Use Copilot to understand algorithms and data structures
- **Code Reviews**: Ask Copilot to review your solutions for improvements
- **Alternative Approaches**: Explore different ways to solve the same problem
- **Documentation**: Let Copilot help write clear docstrings and comments
- **Testing Ideas**: Generate comprehensive test cases for your solutions

## 📝 Daily Solution Template

Each day's solution should follow this structure:

```python
"""
Advent of Code 2024 - Day XX: [Problem Title]

Problem Description:
[Brief description of the problem]

Learning Focus:
[What Python concepts or techniques this problem teaches]
"""

def part_one(input_data: str) -> int:
    """Solve part one of the puzzle."""
    pass

def part_two(input_data: str) -> int:
    """Solve part two of the puzzle."""
    pass

if __name__ == "__main__":
    from utils import read_input
    
    data = read_input("inputs/dayXX.txt")
    
    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")
```

## 🎄 Happy Coding!