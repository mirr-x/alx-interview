#!/usr/bin/python3
"""
    Minimum Operations
"""


def minOperations(n):
    """
        function that calculates the fewest number
        of operations needed to result in exactly
        n H characters in the file
    """
    if n <= 1:
        return 0

    min_ops = [0] * (n + 1)

    for i in range(2, n + 1):
        min_ops[i] = float('inf')

        for j in range(1, i // 2 + 1):
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)

    return min_ops[n]
