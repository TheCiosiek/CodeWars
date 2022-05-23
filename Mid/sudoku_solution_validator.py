def valid_solution(board):
    rows_i = 0
    rows_j = 0
    columns_i = 0
    columns_j = 0
    square_i = 0
    square_j = 0
    check_rows_array = [None] * 10
    check_columns_array = [None] * 10
    check_sq_array = [None] * 10
    #Sprawdzenie wierszy i kolumn
    while rows_i < 9:
        while rows_j < 9:
            if board[rows_i][rows_j] == 0:
                print(False)
                return False
            elif check_rows_array[board[rows_i][rows_j]] == 1 or check_columns_array[board[columns_j][columns_i]] == 1:
                print(False)
                return False
            else: 
                check_rows_array[board[rows_i][rows_j]] = 1
                check_columns_array[board[columns_j][columns_i]] = 1
                rows_j = rows_j + 1
                columns_j = columns_j + 1
        #Empty after iteration
        check_rows_array = [None] * 10
        check_columns_array = [None] * 10

        rows_j = 0
        columns_j = 0
        columns_i = columns_i + 1
        rows_i = rows_i + 1

    #Check 9 squares
    for add_row in range (0, 10, 3):
        for add_col in range (0, 10, 3):
            while square_i < 3:
                while square_j < 3:
                    if check_sq_array[board[square_i+add_row][square_j+add_col]] == 1:
                        print(False)
                        return False
                    else:
                        check_sq_array[board[square_i+add_row][square_j+add_col]] = 1
                        square_j = square_j + 1
                square_j = 0
                square_i = square_i + 1
            check_sq_array.clear()
    print(True)
    return True

# Examples

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]) # => true


valid_solution([
[1, 3, 2, 5, 7, 9, 4, 6, 8],
[4, 9, 8, 2, 6, 1, 3, 7, 5], 
[7, 5, 6, 3, 8, 4, 2, 1, 9],
[6, 4, 3, 1, 5, 8, 7, 9, 2], 
[5, 2, 1, 7, 9, 3, 8, 4, 6], 
[9, 8, 7, 4, 2, 6, 5, 3, 1], 
[2, 1, 4, 9, 3, 5, 6, 8, 7], 
[3, 6, 5, 8, 1, 7, 9, 2, 4],
[8, 7, 9, 6, 4, 2, 1, 3, 5]
]) # => false

# Sudoku Background

# Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
# (More info at: http://en.wikipedia.org/wiki/Sudoku)
# Sudoku Solution Validator

# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
# Examples