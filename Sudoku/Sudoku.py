import random

def clear_screen():
    print("\033[H\033[J", end='')

def print_board(board):
    print("    1 2 3   4 5 6   7 8 9")
    print("  -------------------------")
    for i in range(9):
        print(f"{i + 1} |", end=" ")
        for j in range(9):
            if j == 3 or j == 6:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print("|")
        if i == 2 or i == 5:
            print("  -------------------------")
    print("  -------------------------")

def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def used_in_row(board, row, num):
    return num in board[row]

def used_in_col(board, col, num):
    return num in [board[row][col] for row in range(9)]

def used_in_box(board, box_start_row, box_start_col, num):
    for row in range(box_start_row, box_start_row + 3):
        for col in range(box_start_col, box_start_col + 3):
            if board[row][col] == num:
                return True
    return False

def is_safe(board, row, col, num):
    return not used_in_row(board, row, num) and not used_in_col(board, col, num) and not used_in_box(board, row - row % 3, col - col % 3, num)

def solve_sudoku(board):
    empty_location = find_empty_location(board)
    if not empty_location:
        return True
    row, col = empty_location
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def remove_k_digits(board, k):
    while k > 0:
        i, j = random.randint(0, 8), random.randint(0, 8)
        if board[i][j] != 0:
            board[i][j] = 0
            k -= 1

def generate_sudoku(difficulty):
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    def fill_diagonal_boxes():
        for i in range(0, 9, 3):
            fill_box(i, i)
    
    def fill_box(row, col):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                board[row + i][col + j] = nums.pop()
    
    fill_diagonal_boxes()
    solve_sudoku(board)
    
    if difficulty == 'easy':
        remove_k_digits(board, 20)
    elif difficulty == 'medium':
        remove_k_digits(board, 40)
    elif difficulty == 'hard':
        remove_k_digits(board, 60)
    
    return board

def play():
    clear_screen()
    print("Welcome to Sudoku!")
    difficulty = ''
    while difficulty not in ['easy', 'medium', 'hard']:
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()

    board = generate_sudoku(difficulty)
    original_board = [row[:] for row in board]
    
    while True:
        clear_screen()
        print_board(board)
        move = input("Enter row (1-9), column (1-9), and number (1-9) separated by spaces, or '0 0 0' to quit: ")
        try:
            row, col, num = map(int, move.split())
            if row == 0 and col == 0 and num == 0:
                print("Goodbye!")
                break
            if original_board[row-1][col-1] == 0 and is_safe(board, row-1, col-1, num):
                board[row-1][col-1] = num
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter three numbers separated by spaces.")

if __name__ == "__main__":
    play()