def solve_n_queens(n):
    board = [[0]*n for _ in range(n)]

    # Branch & Bound helpers
    col_used = [False] * n
    diag1 = [False] * (2*n)      # row + col
    diag2 = [False] * (2*n)      # row - col + n

    def solve(row):
        if row == n:
            return True

        for col in range(n):
            # Check if safe
            if (not col_used[col] and
                not diag1[row + col] and
                not diag2[row - col + n]):

                # place queen
                board[row][col] = 1
                col_used[col] = True
                diag1[row + col] = True
                diag2[row - col + n] = True

                # recursive call
                if solve(row + 1):
                    return True

                # backtrack
                board[row][col] = 0
                col_used[col] = False
                diag1[row + col] = False
                diag2[row - col + n] = False

        return False

    if solve(0):
        print("\nSolution:")
        for row in board:
            print(row)
    else:
        print("No solution exists")


# -------- Run --------
n = int(input("Enter value of N: "))
solve_n_queens(n)