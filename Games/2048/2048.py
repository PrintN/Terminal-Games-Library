import random
import curses

SIZE = 4  
INITIAL_TILES = 2  
UP_KEY = 'w'
DOWN_KEY = 's'
LEFT_KEY = 'a'
RIGHT_KEY = 'd'

score = 0

def initialize_board():
    board = [[0] * SIZE for _ in range(SIZE)]
    for _ in range(INITIAL_TILES):
        add_new_tile(board)
    return board

def add_new_tile(board):
    x, y = random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)
    while board[x][y] != 0:
        x, y = random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)
    board[x][y] = random.choice([2, 4])

def print_board(stdscr, board):
    global score
    stdscr.clear()
    
    for i in range(SIZE):
        for j in range(SIZE):
            tile = str(board[i][j]) if board[i][j] != 0 else '.'
            stdscr.addstr(i, j * 6, tile.center(5))  
    stdscr.addstr(SIZE, 0, f"Score: {score}")
    stdscr.addstr(SIZE + 1, 0, "Use WASD or Arrow keys to move. Press 'q' to quit.")
    stdscr.refresh()

def combine_tiles_left(row):
    global score
    new_row = [0] * SIZE
    idx = 0
    for tile in row:
        if tile != 0:
            if idx > 0 and new_row[idx - 1] == tile:
                new_row[idx - 1] *= 2
                score += new_row[idx - 1]
            else:
                new_row[idx] = tile
                idx += 1
    return new_row

def move_left(board):
    for i in range(SIZE):
        board[i] = combine_tiles_left(board[i])
    add_new_tile(board)

def move_right(board):
    for i in range(SIZE):
        board[i].reverse()
        board[i] = combine_tiles_left(board[i])
        board[i].reverse()

def move_up(board):
    transposed_board = [list(row) for row in zip(*board)]
    for i in range(SIZE):
        transposed_board[i] = combine_tiles_left(transposed_board[i])
    for i in range(SIZE):
        for j in range(SIZE):
            board[j][i] = transposed_board[i][j]
    add_new_tile(board)

def move_down(board):
    transposed_board = [list(row) for row in zip(*board)]
    for i in range(SIZE):
        transposed_board[i].reverse()
        transposed_board[i] = combine_tiles_left(transposed_board[i])
        transposed_board[i].reverse()
    for i in range(SIZE):
        for j in range(SIZE):
            board[j][i] = transposed_board[i][j]
    add_new_tile(board)

def check_game_over(board):
    for row in board:
        if 0 in row:
            return False
    for i in range(SIZE):
        for j in range(SIZE):
            if (j < SIZE - 1 and board[i][j] == board[i][j + 1]) or (i < SIZE - 1 and board[i][j] == board[i + 1][j]):
                return False
    return True

def main(stdscr):
    global score
    curses.curs_set(0)  
    curses.raw()  
    stdscr.clear()
    stdscr.refresh()

    board = initialize_board()
    score = 0
    game_over = False

    while not game_over:
        print_board(stdscr, board)

        if check_game_over(board):
            stdscr.addstr(SIZE + 2, 0, "Game Over! Press 'r' to restart or 'q' to quit.")
            stdscr.refresh()
            game_over = True
            continue

        key = stdscr.getch()

        if key in [ord('q')]: 
            return
        elif key in [ord(UP_KEY), curses.KEY_UP]:
            move_up(board)
        elif key in [ord(DOWN_KEY), curses.KEY_DOWN]:
            move_down(board)
        elif key in [ord(LEFT_KEY), curses.KEY_LEFT]:
            move_left(board)
        elif key in [ord(RIGHT_KEY), curses.KEY_RIGHT]:
            move_right(board)

    while game_over:
        key = stdscr.getch()
        if key in [ord('r')]:  
            game_over = False
            board = initialize_board()
            score = 0
        elif key in [ord('q')]:  
            return

if __name__ == "__main__":
    curses.wrapper(main)