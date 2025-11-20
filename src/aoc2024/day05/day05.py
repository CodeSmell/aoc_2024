from aoc2024.utils import read_lines

def part_one(filename: str) -> int:
    """
    Solve part one of day 05.
    
    Args:
        filename: Path to the input file
        
    Returns:
        The solution for part one
    """
    lines = read_lines(filename)
    # TODO: Implement part one solution
    return 0

def part_two(filename: str) -> int:
    """
    Solve part two of day 05.
    
    Args:
        filename: Path to the input file
        
    Returns:
        The solution for part two
    """
    lines = read_lines(filename)
    # TODO: Implement part two solution
    return 0

if __name__ == "__main__":
    # Test with sample data first
    sample_result_part1 = part_one("inputs/day05.sample.txt")
    print(f"Part 1 (sample): {sample_result_part1}")
    
    # Run with actual data
    result_part1 = part_one("inputs/day05.txt")
    print(f"Part 1: {result_part1}")
    
    # Test part 2 with sample data
    sample_result_part2 = part_two("inputs/day05.sample.txt")
    print(f"Part 2 (sample): {sample_result_part2}")
    
    # Run part 2 with actual data
    result_part2 = part_two("inputs/day05.txt")
    print(f"Part 2: {result_part2}")