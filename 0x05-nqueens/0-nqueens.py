#!/usr/bin/python3
"""
N queens
"""
import sys


def is_safe(board, row, col, N):
    """ Check if it's safe to place a queen at board[row][col] """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N):
    """ Utility function to solve N Queens problem """
    # Base case: If all queens are placed then return true
    if col >= N:
        print_solution(board, N)
        return True

    # Consider this column and try placing this queen in all rows one by one
    res = False
    for i in range(N):
        # Check if the queen can be placed on board[i][col]
        if is_safe(board, i, col, N):
            # Place the queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            res = solve_nqueens_util(board, col + 1, N) or res

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen from board[i][col]
            board[i][col] = 0

    # If queen can not be placed in any row in column col, then return false
    return res


def solve_nqueens(N):
    """ Main function to solve N Queens problem """
    # Create a N x N chessboard
    board = [[0] * N for _ in range(N)]

    # Call the utility function to solve N Queens problem
    if not solve_nqueens_util(board, 0, N):
        print("No solution exists")


def print_solution(board, N):
    """ Print the solution """
    res = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                res.append([i, j])
    print(res)


if __name__ == "__main__":
    # Validate command line arguments
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solve_nqueens(N)
