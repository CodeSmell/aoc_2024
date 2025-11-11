from aoc2024.utils import read_lines

'''
Within each pair, figure out how far apart the two numbers are; 
you'll need to add up all of those distances. 
For example, 3 and 7 as input give the distance apart as 4; 
if you pair up a 9 with a 3, the distance apart is 6.
'''
def distance(point1, point2):
    return abs(point2 - point1)

'''
read the day01 input 
each line in the file contains two integers separated by one or more spaces
we want two lists: one for the integers are the left and one for the integers on the right
'''
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