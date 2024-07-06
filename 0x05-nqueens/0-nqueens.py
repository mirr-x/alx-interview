#!/usr/bin/python3
"""
A module for solving the N Queens problem.
"""

import sys


def solve_queens(n):
    """
    Solves the N Queens problem for a given board size `n`.
    """
    column = set()
    pos_diag = set()
    neg_diag = set()

    results = []
    board = [[False] * n for _ in range(n)]

    def backtrack(r):
        """
        Recursively attempts to place queens row by row.
        """
        if r == n:
            results.append([row[:] for row in board])
            return

        for c in range(n):
            if c in column or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            column.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = True

            backtrack(r + 1)

            column.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = False

    backtrack(0)
    return results


def transform_boolean_matrix(matrix):
    """
    Transforms a boolean matrix representing a chessboard
     into a list of row-column pairs where queens are placed.
    """
    result = []
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value:
                result.append([row_index, col_index])
    return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    inp = 0
    try:
        inp = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if inp < 4:
        print("N must be at least 4")
        exit(1)

    results_matrix = solve_queens(inp)

    for r in results_matrix:
        print(transform_boolean_matrix(r))