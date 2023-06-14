# task_11.py

from prettytable import PrettyTable

def is_valid(board, row, col, num):
    """
    Check if it's valid to place a number in a specific cell on a Sudoku board.

    This function checks if the given number is already present in the same
    row, column, or 3x3 box.

    :param board: A 9x9 list of lists representing the Sudoku board.
    :param row: Integer representing the row index.
    :param col: Integer representing the column index.
    :param num: Integer, the number to be placed.
    :return: Boolean, True if it's valid to place the number, False otherwise.
    """

    # Check if the number is in the given row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(board):
    """
    Solve a Sudoku puzzle by filling the empty cells.

    Empty cells are denoted by 0. The function uses a backtracking algorithm.

    :param board: A 9x9 list of lists representing the Sudoku board.
    :return: Boolean, True if the Sudoku puzzle is successfully solved, False otherwise.
    """

    # Find an empty position (denoted by 0)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try numbers from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        # Recursively try to fill in the rest
                        if solve_sudoku(board):
                            return True

                        # If the recursion failed, reset the cell to 0 and backtrack
                        board[row][col] = 0

                # If no number can be placed, the Sudoku can't be solved
                return False

    # If the entire board is filled, the Sudoku is solved
    return True



def print_sudoku_board(board):
    """
    Prints a given Sudoku board in a formatted table.
    
    The function uses PrettyTable to format the board. Each cell in the board is 
    centered, and horizontal lines are added between rows. Vertical lines are 
    inserted after every 3 columns to demarcate the 3x3 Sudoku boxes.
    
    :param board: A 9x9 list of lists representing the Sudoku board,
                  where 0 represents an empty cell.
    """

    table = PrettyTable()

    # Disable the table headers
    table.header = False

    # Set the alignment to center
    table.align = 'c'

    # Add horizontal lines between rows
    table.hrules = 1

    # Add rows to the table
    for row in board:
        formatted_row = []
        for j, cell in enumerate(row):
            # Adding vertical line after every 3 columns
            if j % 3 == 0 and j > 0:
                formatted_row.append('||')
            formatted_row.append(str(cell) if cell != 0 else ' ')
        table.add_row(formatted_row)

    # Print the table
    print(table)

# Example Sudoku board
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Print the Sudoku board
print_sudoku_board(sudoku_board)

# Solve the Sudoku
if solve_sudoku(sudoku_board):
    
    # Output the solved Sudoku
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists")

# Print the Sudoku board Final output
print_sudoku_board(sudoku_board)