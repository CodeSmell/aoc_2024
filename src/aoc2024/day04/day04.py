from aoc2024.utils import read_input
#
# ThisThe puzzle is a word search that allows words to be 
# horizontal, vertical, diagonal, written backwards, 
# or even overlapping other words
#

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

# AI generated cross word finder (several iterations to optimize and make readable)
def count_crossing_word(rows, word):
    count = 0
    if not rows or not rows[0]:
        return count

    num_rows = len(rows)
    num_columns = len(rows[0]) if num_rows > 0 else 0
    word_length = len(word)
    half_word_length = (word_length // 2)

    def diagonal_at(center_row, center_col, row_direction, col_direction):
        """
        Extracts a diagonal word centered at (center_row, center_col).
        
        Args:
            center_row: Row index of the center position
            center_col: Column index of the center position  
            row_direction: 1 for down, -1 for up
            col_direction: 1 for right, -1 for left
            
        Returns:
            String representing the diagonal word
        """
        diagonal_chars = []
        
        # Start from the beginning of the word (half_word_length positions back from center)
        start_row = center_row - half_word_length * row_direction
        start_col = center_col - half_word_length * col_direction
        
        # Extract each character of the word
        for i in range(word_length):
            current_row = start_row + i * row_direction
            current_col = start_col + i * col_direction
            diagonal_chars.append(rows[current_row][current_col])
            
        return ''.join(diagonal_chars)

    count = 0
    for r in range(half_word_length, num_rows - half_word_length):
        for c in range(half_word_length, num_columns - half_word_length):
            diag1 = diagonal_at(r, c, 1, 1)   # ↘
            diag2 = diagonal_at(r, c, 1, -1)  # ↙
            if ((diag1 == word or diag1 == word[::-1]) and
                (diag2 == word or diag2 == word[::-1])):
                count += 1
    return count

def part_one(data: str) -> int:
    word_to_find = "XMAS"
    count = 0
    rows = data.splitlines()
    # rows
    count += search_lines(rows, word_to_find)
    # columns
    columns = get_columns(rows)
    count += search_lines(columns, word_to_find)
    #diagonals
    diagonals = get_diagonals(rows)
    count += search_lines(diagonals, word_to_find)
    return count

def part_two(data: str) -> int:
    return count_crossing_word(data.splitlines(), "MAS")

if __name__ == "__main__":
    data = read_input("inputs/day04.txt")
    # result_part1 = part_one(data)
    # print(f"Part 1: {result_part1}")
    
    result_part2 = part_two(data)
    print(f"Part 2: {result_part2}")