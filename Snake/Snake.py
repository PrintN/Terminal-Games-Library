import os
import sys
import time
import random
import platform
import threading

class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def init_board(width, height):
    board = [[' ' for _ in range(width)] for _ in range(height)]
    for y in range(width):
        board[0][y] = Colors.RED + '█' + Colors.RESET
        board[height - 1][y] = Colors.RED + '█' + Colors.RESET
    for x in range(height):
        board[x][0] = Colors.RED + '█' + Colors.RESET
        board[x][width - 1] = Colors.RED + '█' + Colors.RESET
    return board

def draw_elements(board, snake, food):
    for y in range(1, len(board) - 1):
        for x in range(1, len(board[0]) - 1):
            if board[y][x] not in [Colors.RED + '█' + Colors.RESET]:
                board[y][x] = ' '

    for y, x in snake:
        if 0 <= y < len(board) and 0 <= x < len(board[0]):
            board[y][x] = Colors.GREEN + '🟩' + Colors.RESET

    fy, fx = food
    if 0 <= fy < len(board) and 0 <= fx < len(board[0]):
        board[fy][fx] = Colors.YELLOW + '🍎' + Colors.RESET

def print_board(board):
    clear_screen()
    for row in board:
        print(''.join(row))
    print(f"{Colors.CYAN}Score: {score}{Colors.RESET}")


def init_game():
    width = 50
    height = 20
    board = init_board(width, height)
    snake = [(height // 2, width // 2), (height // 2, width // 2 - 1), (height // 2, width // 2 - 2)]
    food = (random.randint(1, height - 2), random.randint(1, width - 2))
    direction = 'RIGHT'
    return board, snake, food, direction, width, height

def handle_input(direction):
    if platform.system() == 'Windows':
        import msvcrt
        while True:
            key = msvcrt.getch()
            if key == b'H': 
                direction[0] = 'UP'
            elif key == b'P':  
                direction[0] = 'DOWN'
            elif key == b'K':  
                direction[0] = 'LEFT'
            elif key == b'M': 
                direction[0] = 'RIGHT'
    else:
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            while True:
                ch = sys.stdin.read(1)
                if ch == 'w': direction[0] = 'UP'
                elif ch == 's': direction[0] = 'DOWN'
                elif ch == 'a': direction[0] = 'LEFT'
                elif ch == 'd': direction[0] = 'RIGHT'
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def check_collision(snake, height, width):
    head = snake[0]
    y, x = head
    if y <= 0 or y >= height - 1 or x <= 0 or x >= width - 1 or head in snake[1:]:
        return True
    return False

def main():
    global score
    board, snake, food, direction, width, height = init_game()

    direction = [direction]
    input_thread = threading.Thread(target=handle_input, args=(direction,))
    input_thread.daemon = True
    input_thread.start()

    global score
    score = 0

    while True:
        draw_elements(board, snake, food)
        print_board(board)

        head_y, head_x = snake[0]
        if direction[0] == 'UP':
            head_y -= 1
        elif direction[0] == 'DOWN':
            head_y += 1
        elif direction[0] == 'LEFT':
            head_x -= 1
        elif direction[0] == 'RIGHT':
            head_x += 1
        
        new_head = (head_y, head_x)
        snake.insert(0, new_head)
        
        if new_head == food:
            food = (random.randint(1, height - 2), random.randint(1, width - 2))
            score += 1
        else:
            snake.pop()
        
        if check_collision(snake, height, width):
            print(f"{Colors.RED}Game Over!{Colors.RESET}")
            break
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()