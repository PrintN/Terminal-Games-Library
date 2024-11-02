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

def play_crash(balance):
    clear_screen()
    print("Welcome to Crash!")
    print(f"Your current balance: ${balance}")
    bet = int(input("Enter your bet amount: "))

    if bet > balance:
        print(f"{Colors.RED}You don't have enough balance!{Colors.RESET}")
        return balance

    multiplier = 1.0
    crash_point = random.uniform(1.5, 5.0)
    
    print("The game is starting...")
    time.sleep(2)
    
    while True:
        clear_screen()
        print(f"Multiplier: {multiplier:.2f}x")
        user_input = input("Press 'c' to cash out or Enter to continue: ")
        
        if user_input.lower() == 'c':
            winnings = bet * multiplier
            print(f"{Colors.GREEN}Congratulations! You cashed out at {multiplier:.2f}x and won ${winnings:.2f}.{Colors.RESET}")
            balance += winnings
            break
        
        multiplier += random.uniform(0.1, 0.5)
        
        if multiplier >= crash_point:
            print(f"{Colors.RED}Crash! You lost ${bet}.{Colors.RESET}")
            balance -= bet
            break
        
        time.sleep(1)

    return balance

if __name__ == "__main__":
    balance = 100
    balance = play_crash(balance)