import random
import sys

def clear_screen():
    print("\033[H\033[J", end='')

def delete_last_line(n=1): 
    for _ in range(n): 
        sys.stdout.write('\x1b[1A') 
        sys.stdout.write('\x1b[2K') 

def determine_winner(choice1, choice2, player1_name="Player 1", player2_name="Player 2"):
    outcomes = {
        "rock": {"scissors": f"Rock smashes scissors! {player1_name} won!", "paper": f"Paper covers rock! {player2_name} won!"},
        "paper": {"rock": f"Paper covers rock! {player1_name} won!", "scissors": f"Scissors cuts paper! {player2_name} won!"},
        "scissors": {"paper": f"Scissors cuts paper! {player1_name} won!", "rock": f"Rock smashes scissors! {player2_name} won!"}
    }
    if choice1 == choice2:
        return f"Both players selected {choice1}. It's a tie!"
    return outcomes.get(choice1, {}).get(choice2, "Invalid choice.")

def play():
    clear_screen()
    start = input("Welcome to Rock Paper Scissors! For Player vs Bot (press 1) for Player vs Player (press 2): ")
    
    if start == "1":
        user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
        moves = ["rock", "paper", "scissors"]
        bot_choice = random.choice(moves)
        print(f"\nYou chose {user_choice}, bot chose {bot_choice}.\n")
        print(determine_winner(user_choice, bot_choice, "You", "Bot"))
    
    elif start == "2":
        player1_choice = input("Player 1 (rock, paper, scissors)? ").lower()
        delete_last_line()
        player2_choice = input("Player 2 (rock, paper, scissors)? ").lower()
        print(determine_winner(player1_choice, player2_choice))
    
    else:
        print("Invalid option.")

if __name__ == "__main__":
    play()