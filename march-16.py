# interview question: given a list of integers, return the largest product of any three integers in the list
def largest_product_of_three(nums):
    nums.sort()
    n = len(nums)
    # The largest product can be either:
    # 1. Product of three largest numbers
    # 2. Product of two smallest (most negative) and the largest number
    return max(nums[0] * nums[1] * nums[n-1], nums[n-3] * nums[n-2] * nums[n-1])
# Example usage
nums = [-10, -10, 5, 2]
print(largest_product_of_three(nums))  # Output: 500

# 2. N-Queens problem: place N queens on an N x N chessboard such that no two queens threaten each other
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True
    def solve_n_queens_util(board, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve_n_queens_util(board, row + 1)
    result = []
    solve_n_queens_util([-1] * n, 0)
    return result
# Example usage
n = 4
solutions = solve_n_queens(n)
for solution in solutions:
    print(solution)  # Output: [[1, 3, 0, 2], [2, 0, 3, 1]]
    
#