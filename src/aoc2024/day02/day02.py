from aoc2024.utils.file_io import read_lines

def is_safe_range(level1, level2):
    return 1 <= abs(level1 - level2) <= 3

# a safe report with toleration for one bad level
def is_safe_report_toleration(levels):
    is_safe = is_safe_report(levels)

    if not is_safe:
        # remove a level and check entire report again
        for index in range(len(levels)): 
            new_levels = levels[:index] + levels[index + 1 :]
            is_safe = is_safe_report(new_levels)
            if is_safe:
                break

    return is_safe

# Define a function to check if a range is safe
# a report is safe if the levels are either all increasing or all decreasing.
def is_safe_report(levels):
    # A report with less than 2 levels is trivially safe
    if len(levels) < 2:
        return True

    is_safe = False

    # check if increasing or decreasing
    decreasing = False
    if levels[0] > levels[1]:
        decreasing = True
    
    for index in range(len(levels) - 1):
        val1 = levels[index]
        val2 = levels[index + 1]
        
        if decreasing and val1 > val2:
            is_safe = is_safe_range(val1, val2)
        elif not decreasing and val1 < val2:
            is_safe = is_safe_range(val1, val2)
        else:
            is_safe = False

        # if any pair is not safe, the report is not safe
        if not is_safe:
            break
        
    return is_safe

# tolerate a single bad level 
def part_two(reports):
    safe_count = 0
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe_report_toleration(levels):
            safe_count += 1
    return safe_count

# find the safe reports
def part_one(reports):
    safe_count = 0
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe_report(levels):
            safe_count += 1
    return safe_count

# Run the solution if this file is executed directly
if __name__ == "__main__":
    reports = read_lines("inputs/day02.txt")
    # print(f"Part 1: {part_one(reports)}")
    print(f"Part 2: {part_two(reports)}")