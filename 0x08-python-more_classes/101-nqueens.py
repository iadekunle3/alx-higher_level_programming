#!/usr/bin/python3
# Function to solve the N-Queens problem
def solve_n_queen(n):
    # Nested function to check if a queen can be placed at a given position
    def is_safe(queen_number, position):
        # Loop over all queens to the left of the current queen
        for i in range(queen_number):
            # Check if another queen is in the same row or on the same diagonal
            if (queens[i] == position or
                    queens[i] - i == position - queen_number or
                    queens[i] + i == position + queen_number):
                return False
        return True

    # Nested function to place queens one by one, starting from the left
    def place_queen(queen_number, n):
        # If all queens are placed correctly, print the solution
        if queen_number == n:
            result.append(queens[:])
            return
        # Try to place a queen in each row of the current column
        for i in range(n):
            # If the queen can be placed at the current position, place it
            if is_safe(queen_number, i):
                queens[queen_number] = i
                # Place the rest of the queens
                place_queen(queen_number + 1, n)

    # Initialize the result list and the queens list
    result = []
    queens = [-1] * n
    # Start placing queens from the first column
    place_queen(0, n)
    return result
