import re
from aoc2024.utils.file_io import read_input

pattern = r"mul\(\d{1,3},\d{1,3}\)"
pattern_group = r"mul\((\d{1,3}),(\d{1,3})\)"
pattern_conditional_group = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"

def find_good_commands(corrupted_memory):
    matches = re.findall(pattern_conditional_group, corrupted_memory)
    return matches

# given list of good commands, 
# run them and return sum of their results
def run_good_commands(commands, use_conditionals):
    total = 0
    # default is run commands
    runCommand = True

    for command in commands:
        if use_conditionals:
            if command == "do()":
                runCommand = True
                continue
            elif command == "don't()":
                runCommand = False
                continue

        # the number pairs are captured in groups
        if runCommand:
            match = re.match(pattern_group, command)
            if match:
                x, y = match.groups()
                result = mul((x, y))
                total += result
    return total

def mul(tuple_xy):
    x, y = map(int, tuple_xy)
    return x * y

def part_one(data):
    commands = find_good_commands(data)
    return run_good_commands(commands, False)

def part_two(data):
    commands = find_good_commands(data)
    return run_good_commands(commands, True)

if __name__ == "__main__":
    data = read_input("inputs/day03.txt")
    # print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")
