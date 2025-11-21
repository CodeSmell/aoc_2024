from aoc2024.utils import read_input
#
# ThisThe puzzle is a word search that allows words to be 
# horizontal, vertical, diagonal, written backwards, 
# or even overlapping other words
#

WORD_TO_FIND = "XMAS"

# once a line is isolated look for the word in both directions
def count_word_in_line(line: str, word: str) -> int:
    count = 0
    x = len(line) - len(word) + 1
    for i in range(x):
        if line[i:i+len(word)] == word:
            count += 1
        elif line[i:i+len(word)] == word[::-1]:
            count += 1
    return count

# given a list of lines (which could be the rows,
# columns or diagonals in data), 
# search each line for the word
def search_lines(lines: list[str], word: str):
    count = 0
    # find word in lines
    for line in lines:
        count += count_word_in_line(line, word)
    return count

def get_columns(rows: list[str]) -> list[str]:
    columns = []
    if not rows or not rows[0]:
        pass
    else:
        len_each_line = len(rows[0])
        for col in range(len_each_line):
            column = ''.join(row[col] for row in rows)
            columns.append(column)    
    return columns

def get_diagonals(lines: list[str]) -> list[str]:
    if not lines or not lines[0]:
        return []
    
    num_rows = len(lines)
    num_cols = len(lines[0])
    diagonals = []
    
    # Helper function to extract a diagonal given starting position and direction
    def extract_diagonal(start_row: int, start_col: int, row_step: int, col_step: int) -> str:
        diagonal = ""
        row_idx, col_idx = start_row, start_col
        while 0 <= row_idx < num_rows and 0 <= col_idx < num_cols:
            diagonal += lines[row_idx][col_idx]
            row_idx += row_step
            col_idx += col_step
        return diagonal
    
    # Top-left to bottom-right diagonals (↘): row+1, col+1
    # Start from first column (each row)
    for start_row in range(num_rows):
        diagonal = extract_diagonal(start_row, 0, 1, 1)
        if diagonal:
            diagonals.append(diagonal)
    
    # Start from first row (each column, skip first to avoid duplicate)
    for start_col in range(1, num_cols):
        diagonal = extract_diagonal(0, start_col, 1, 1)
        if diagonal:
            diagonals.append(diagonal)
    
    # Top-right to bottom-left diagonals (↙): row+1, col-1
    # Start from last column (each row)
    for start_row in range(num_rows):
        diagonal = extract_diagonal(start_row, num_cols - 1, 1, -1)
        if diagonal:
            diagonals.append(diagonal)
    
    # Start from first row (each column, skip last to avoid duplicate)
    for start_col in range(num_cols - 2, -1, -1):
        diagonal = extract_diagonal(0, start_col, 1, -1)
        if diagonal:
            diagonals.append(diagonal)
    
    return diagonals

def part_one(data: str) -> int:
    count = 0
    rows = data.splitlines()
    # rows
    count += search_lines(rows, WORD_TO_FIND)
    # columns
    columns = get_columns(rows)
    count += search_lines(columns, WORD_TO_FIND)
    #diagonals
    diagonals = get_diagonals(rows)
    count += search_lines(diagonals, WORD_TO_FIND)
    return count

def part_two(data: str) -> int:
    pass

if __name__ == "__main__":
    data = read_input("inputs/day04.txt")
    result_part1 = part_one(data)
    print(f"Part 1: {result_part1}")
    
    # result_part2 = part_two(data)
    # print(f"Part 2: {result_part2}")