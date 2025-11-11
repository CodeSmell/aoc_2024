from aoc2024.utils import read_lines

"""
Within each pair, figure out how far apart the two numbers are; 
you'll need to add up all of those distances. 
For example, 3 and 7 as input give the distance apart as 4; 
if you pair up a 9 with a 3, the distance apart is 6.
"""
def distance(point1, point2):
    return abs(point2 - point1)


"""
read the day01 input 
each line in the file contains two integers separated by one or more spaces
we want two lists: one for the integers are the left and one for the integers on the right
"""
def read_day01_input(filename):
    left_numbers = []
    right_numbers = []

    lines = read_lines(filename)
    for line in lines:
        parts = line.split()
        if len(parts) == 2:
            left_numbers.append(int(parts[0]))
            right_numbers.append(int(parts[1]))

    # returns a tuple of two lists
    return left_numbers, right_numbers

'''
Pair up the smallest number in the left list with the smallest number in the right list, 
then the second-smallest left number with the second-smallest right number, and so on.
'''
def pair_and_sum_distances(left_numbers, right_numbers):
    sorted_left = sorted(left_numbers)
    sorted_right = sorted(right_numbers)

    total_distance = 0
    # pair up corresponding elements using zip 
    for left, right in zip(sorted_left, sorted_right):
        total_distance += distance(left, right)

    return total_distance

def part_one(filename):
    left_numbers, right_numbers = read_day01_input(filename)
    total_distance = pair_and_sum_distances(left_numbers, right_numbers)
    return total_distance

# Run the solution if this file is executed directly
if __name__ == "__main__":
    print(f"Part 1: {part_one("inputs/day01.txt")}")