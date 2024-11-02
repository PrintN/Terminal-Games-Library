import random

def print_board(board):
    """Prints the current board state."""
    size = 3
    for row in range(size):
        row_display = []
        for col in range(size):
            row_display.append(f" {board[row * size + col]} ")
        print("|".join(row_display))
        if row < size - 1:
            print("---|---|---")

def get_player_input(board, player):
    """Prompts the player for a move and updates the board."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
                return move
            else:
                print("This position is already taken.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number between 1 and 9.")

def get_bot_move(board, difficulty, player):
    """Determines the bot's move based on the selected difficulty."""
    if difficulty in ["easy", "e"]:
        return get_random_move(board)
    elif difficulty in ["medium", "m"]:
        return get_medium_move(board, player)
    elif difficulty in ["hard", "h"]:
        return get_best_move(board, player)

def get_random_move(board):
    """Returns a random valid move."""
    available_moves = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(available_moves)

def get_medium_move(board, player):
    """Returns a move based on medium difficulty strategy."""
    opponent = "O" if player == "X" else "X"
    for move in range(9):
        if board[move] == " ":
            board[move] = player
            if check_winner(board):
                board[move] = " "
                return move
            board[move] = " "
    for move in range(9):
        if board[move] == " ":
            board[move] = opponent
            if check_winner(board):
                board[move] = " "
                return move
            board[move] = " "
    return get_random_move(board)

def get_best_move(board, player):
    """Determines the best move using the minimax algorithm."""
    best_val = -float('inf')
    best_move = -1
    for move in range(9):
        if board[move] == " ":
            board[move] = player
            move_val = minimax(board, 0, False, player)
            board[move] = " "
            if move_val > best_val:
                best_move = move
                best_val = move_val
    return best_move

def minimax(board, depth, is_max, player):
    """Minimax algorithm for finding the best move."""
    opponent = "O" if player == "X" else "X"
    if check_winner(board):
        return 10 - depth if not is_max else depth - 10
    if " " not in board:
        return 0

    if is_max:
        best_val = -float('inf')
        for move in range(9):
            if board[move] == " ":
                board[move] = player
                best_val = max(best_val, minimax(board, depth + 1, not is_max, player))
                board[move] = " "
        return best_val
    else:
        best_val = float('inf')
        for move in range(9):
            if board[move] == " ":
                board[move] = opponent
                best_val = min(best_val, minimax(board, depth + 1, not is_max, player))
                board[move] = " "
        return best_val

def check_winner(board):
    """Checks if there is a winner."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertical
        [0, 4, 8], [2, 4, 6]             # diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return True
    return False

def play_game(game_mode, difficulty):
    """Main game loop."""
    board = [" " for _ in range(9)]
    current_player = "X"
    for _ in range(9):
        print_board(board)
        if game_mode in ["yes", "y"] and current_player == "O":
            move = get_bot_move(board, difficulty, current_player)
            board[move] = current_player
            print(f"Bot chose position {move + 1}")
        else:
            move = get_player_input(board, current_player)
            print(f"Player {current_player} chose position {move + 1}")
        
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a tie!")

def tic_tac_toe():
    """Starts the Tic Tac Toe game."""
    while True:
        game_mode = input("Do you want to play against a bot? (Yes / No): ").strip().lower()
        if game_mode in ["yes", "y"]:
            while True:
                difficulty = input("Select difficulty (Easy / Medium / Hard): ").strip().lower()
                if difficulty in ["easy", "medium", "hard", "e", "m", "h"]:
                    break
                else:
                    print("Invalid difficulty. Please enter a valid difficulty.")
        elif game_mode in ["no", "n"]:
            difficulty = None
        else:
            print("Invalid answer. Please enter a valid answer.")
            continue

        play_game(game_mode, difficulty)

        again = input("Do you want to play again, change gamemode, or quit? (Play / Change / Quit): ").strip().lower()
        if again in ["quit", "q"]:
            break
        elif again in ["change", "c"]:
            continue
        elif again not in ["play", "p"]:
            print("Invalid option. Exiting the game.")
            break

tic_tac_toe()