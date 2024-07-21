import os
import platform
import random
import sys

class Colors:
    RESET = '\033[0m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CLEAR_LINE = '\033[K'  
    CURSOR_UP = '\033[A'  

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_message(message, end='\n'):
    sys.stdout.write(message + end)
    sys.stdout.flush()

def play_guess_the_number():
    clear_screen()
    print("Welcome to Guess the Number!")
    
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))

            if lower_bound >= upper_bound:
                print_message(f"{Colors.RED}Invalid range. The upper bound must be greater than the lower bound.{Colors.RESET}")
                continue

            target_number = random.randint(lower_bound, upper_bound)
            attempts = 0
            max_attempts = 10 

            print_message(f"Guess the number between {lower_bound} and {upper_bound} (inclusive). You have {max_attempts} attempts.")
            
            while attempts < max_attempts:
                try:
                    print_message(f"Attempt {attempts + 1}/{max_attempts}: ", end='')
                    guess = int(input())
                    
                    sys.stdout.write(Colors.CLEAR_LINE)
                    
                    if guess < lower_bound or guess > upper_bound:
                        sys.stdout.write(Colors.CURSOR_UP)
                        sys.stdout.write(Colors.CLEAR_LINE)
                        print_message(f"{Colors.RED}Your guess is out of bounds. Please enter a number between {lower_bound} and {upper_bound}.{Colors.RESET}", end='')
                    elif guess < target_number:
                        sys.stdout.write(Colors.CURSOR_UP)
                        sys.stdout.write(Colors.CLEAR_LINE)
                        print_message(f"{Colors.YELLOW}Too low! Try again.{Colors.RESET}", end='')
                    elif guess > target_number:
                        sys.stdout.write(Colors.CURSOR_UP)
                        sys.stdout.write(Colors.CLEAR_LINE)
                        print_message(f"{Colors.YELLOW}Too high! Try again.{Colors.RESET}", end='')
                    else:
                        print_message(f"{Colors.GREEN}Congratulations! You guessed the number {target_number} in {attempts + 1} attempts.{Colors.RESET}")
                        break
                    attempts += 1
                except ValueError:
                    sys.stdout.write(Colors.CURSOR_UP)
                    sys.stdout.write(Colors.CLEAR_LINE)
                    print_message(f"{Colors.RED}Invalid input. Please enter a valid integer.{Colors.RESET}", end='')

            if attempts == max_attempts:
                print_message(f"{Colors.RED}Sorry, you've used all your attempts. The number was {target_number}.{Colors.RESET}")

        except ValueError:
            print_message(f"{Colors.RED}Invalid input. Please enter valid integers for the bounds.{Colors.RESET}")
        
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            break

if __name__ == "__main__":
    play_guess_the_number()
