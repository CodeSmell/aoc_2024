import re
from aoc2024.utils.file_io import read_input

# AI suggested naming convention
# and compiling patterns for larger inputs
PATTERN_MUL = r"mul\(\d{1,3},\d{1,3}\)"
PATTERN_MUL_GROUP = r"mul\((\d{1,3}),(\d{1,3})\)"
PATTERN_CONDITIONAL_GROUP = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"

def find_good_commands(corrupted_memory:str) -> list[str]:
    matches = re.findall(PATTERN_CONDITIONAL_GROUP, corrupted_memory)
    return matches

# given list of good commands, 
# run them and return sum of their results
def run_good_commands(commands: list[str], use_conditionals: bool) -> int:
    total = 0
    # default is run commands
    run_command_mode = True

    for command in commands:
        if use_conditionals:
            if command == "do()":
                run_command_mode = True
                continue
            elif command == "don't()":
                run_command_mode = False
                continue

        # the number pairs are captured in groups
        if run_command_mode:
            match = re.match(PATTERN_MUL_GROUP, command)
            if match:
                x, y = match.groups()
                result = mul((x, y))
                total += result
    return total

def mul(tuple_xy):
    x, y = map(int, tuple_xy)
    return x * y

def part_one(data: str) -> int:
    commands = find_good_commands(data)
    return run_good_commands(commands, False)

def part_two(data: str) -> int:
    commands = find_good_commands(data)
    return run_good_commands(commands, True)

if __name__ == "__main__":
    data = read_input("inputs/day03.txt")
    # print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")
