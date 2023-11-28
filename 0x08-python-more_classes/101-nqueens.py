#!/usr/bin/python3
"""

This module contains an algorithm that resolves the N-Queen puzzle
using backtracking

"""


def solveNQueen(n):
""" Method that determines if the queens can or can't kill each other

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number

    Returns:
        True: when queens can't kill each other
        False: when some of the queens can kill

    """
    def isSafe(queen_number, position):
        for i in range(queen_number):
            if queens[i] == position or \
                queens[i] - i == position - queen_number or \
                queens[i] + i == position + queen_number:
                return False
        return True

    def placeQueen(queen_number, n):
        if queen_number == n:
            result.append(queens[:])
            return
        for i in range(n):
            if isSafe(queen_number, i):
                queens[queen_number] = i
                placeQueen(queen_number + 1, n)

    result = []
    queens = [-1] * n
    placeQueen(0, n)
    return result
