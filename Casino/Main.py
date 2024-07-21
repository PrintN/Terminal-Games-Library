import os
import platform
from Games.Slots import play_slots
from Games.Minesweeper import play_minesweeper
from Games.Plinko import play_plinko
from Games.Crash import play_crash

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def display_menu(balance):
    clear_screen()
    print("Welcome to the Terminal Casino!")
    print(f"Your balance: ${balance}")
    print("1. Play Slots")
    print("2. Play Minesweeper")
    print("3. Play Plinko")
    print("4. Play Crash")
    print("5. Exit")

def main():
    balance = 100 
    while True:
        display_menu(balance)
        choice = input("Choose an option: ")

        if choice == '1':
            balance = play_slots(balance)
        elif choice == '2':
            balance = play_minesweeper(balance)
        elif choice == '3':
            balance = play_plinko(balance)
        elif choice == '4':
            balance = play_crash(balance)
        elif choice == '5':
            print(f"Thank you for visiting the Terminal Casino! Your final balance is ${balance}. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()