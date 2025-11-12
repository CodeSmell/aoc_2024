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
calculate how many times each number in the left list appears in the right list
calculate a total similarity score by adding up each number in the left list 
after multiplying it by the number of times that number appears in the right list.
For example, if the number in the left is 3 and it appears in the right list 3 times we get 3*3=9

By way of another example:
if the left list is [3, 4, 2, 3] and the right list is [4,3,5,4]
then the similarity score is 3*1 + 4*2 + 2*0 + 3*1 = 14
"""
def similarity(left_numbers, right_numbers):
    total_similarity = 0
    for number in left_numbers:
        count_in_right = right_numbers.count(number)
        total_similarity += number * count_in_right
    return total_similarity

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

def part_one(left_numbers, right_numbers):
    total_distance = pair_and_sum_distances(left_numbers, right_numbers)
    return total_distance

def part_two(left_numbers, right_numbers):
    total_similarity = similarity(left_numbers, right_numbers)
    return total_similarity

# Run the solution if this file is executed directly
if __name__ == "__main__":
    left_numbers, right_numbers = read_day01_input("inputs/day01.txt")
    print(f"Part 1: {part_one(left_numbers, right_numbers)}")
    print(f"Part 2: {part_two(left_numbers, right_numbers)}")