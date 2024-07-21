import os
import platform
import random
import time

class Colors:
    RESET = '\033[0m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_plinko_board(board):
    clear_screen()
    for row in board:
        print(' '.join(row))
    time.sleep(0.5)

def play_plinko(balance):
    clear_screen()
    print("Welcome to Plinko!")
    print(f"Your current balance: ${balance}")
    bet = int(input("Enter your bet amount: "))

    if bet > balance:
        print(f"{Colors.RED}You don't have enough balance!{Colors.RESET}")
        return balance

    rows = 6
    cols = 7
    board = [['.' for _ in range(cols)] for _ in range(rows)]

    position = cols // 2
    for row in range(rows):
        board[row][position] = 'O'
        print_plinko_board(board)
        board[row][position] = '.'
        position += random.choice([-1, 1])
        if position < 0:
            position = 0
        if position >= cols:
            position = cols - 1

    board[rows - 1][position] = 'O'
    print_plinko_board(board)

    payouts = [0, 1, 2, 5, 2, 1, 0]
    winnings = bet * payouts[position]
    
    if winnings > 0:
        print(f"{Colors.GREEN}Congratulations! You won ${winnings}.{Colors.RESET}")
        balance += winnings
    else:
        print(f"{Colors.RED}Sorry, you didn't win anything. You lost ${bet}.{Colors.RESET}")
        balance -= bet
    
    return balance

if __name__ == "__main__":
    balance = 100 
    balance = play_plinko(balance)