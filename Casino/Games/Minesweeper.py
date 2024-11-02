import os
import platform
import random

class Colors:
    RESET = '\033[0m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_board(board):
    clear_screen()
    for row in board:
        print(' '.join(row))
    print()

def initialize_board(size, mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    for _ in range(mines):
        while True:
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
            if board[row][col] == ' ':
                board[row][col] = 'M'
                break
    return board

def count_adjacent_mines(board, row, col):
    size = len(board)
    mine_count = 0
    for r in range(max(0, row-1), min(size, row+2)):
        for c in range(max(0, col-1), min(size, col+2)):
            if board[r][c] == 'M':
                mine_count += 1
    return mine_count

def reveal_cell(board, visible_board, row, col):
    if visible_board[row][col] != '_':
        return
    if board[row][col] == 'M':
        visible_board[row][col] = Colors.RED + 'M' + Colors.RESET
    else:
        adjacent_mines = count_adjacent_mines(board, row, col)
        visible_board[row][col] = Colors.GREEN + str(adjacent_mines) + Colors.RESET if adjacent_mines > 0 else ' '

def play_minesweeper(balance):
    clear_screen()
    print("Welcome to Minesweeper!")
    size = int(input("Enter board size (e.g., 8 for an 8x8 board): "))
    mines = int(input("Enter number of mines: "))
    
    if mines >= size * size:
        print(f"{Colors.RED}Number of mines must be less than the number of cells on the board!{Colors.RESET}")
        return balance

    board = initialize_board(size, mines)
    visible_board = [['_' for _ in range(size)] for _ in range(size)]
    
    print(f"Your current balance: ${balance}")
    bet = int(input("Enter your bet amount: "))
    
    if bet > balance:
        print(f"{Colors.RED}You don't have enough balance!{Colors.RESET}")
        return balance

    cells_revealed = 0
    total_safe_cells = size * size - mines
    while True:
        print_board(visible_board)
        try:
            action = input("Enter row and column to reveal (e.g., '0 1') or 'stop' to end the game: ")
            if action.lower() == 'stop':
                risk_factor = (size * size) / (size * size - mines)
                winnings = bet * (1 + (cells_revealed / total_safe_cells) * risk_factor)
                print(f"{Colors.GREEN}You revealed {cells_revealed} cells and won ${winnings:.2f}!{Colors.RESET}")
                balance += winnings
                break

            row, col = map(int, action.split())
            if board[row][col] == 'M':
                print(f"{Colors.RED}Boom! You hit a mine. You lost ${bet}. Game Over!{Colors.RESET}")
                balance -= bet
                break
            else:
                reveal_cell(board, visible_board, row, col)
                cells_revealed += 1
        except ValueError:
            print("Invalid input. Please enter row and column as two integers separated by space.")
        except IndexError:
            print("Invalid input. Please enter values within the board size.")
    
    return balance

if __name__ == "__main__":
    balance = 100
    balance = play_minesweeper(balance)