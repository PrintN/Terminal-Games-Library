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

def print_slots(slot1, slot2, slot3, slot4):
    clear_screen()
    print("Spinning...")
    print(f"| {slot1} | {slot2} | {slot3} | {slot4} |")
    time.sleep(0.1)

def play_slots(balance):
    clear_screen()
    print("Welcome to Slots!")
    print(f"Your current balance: ${balance}")
    bet = int(input("Enter your bet amount: "))
    
    if bet > balance:
        print(f"{Colors.RED}You don't have enough balance!{Colors.RESET}")
        return balance
    
    symbols = ['🍒', '🍒', '🍒', '🍋', '🍋', '🔔', '🔔', '⭐', '⭐', '💎']
    
    for _ in range(10):
        slot1 = random.choice(symbols)
        slot2 = random.choice(symbols)
        slot3 = random.choice(symbols)
        slot4 = random.choice(symbols)
        print_slots(slot1, slot2, slot3, slot4)

    slot1 = random.choice(symbols)
    slot2 = random.choice(symbols)
    slot3 = random.choice(symbols)
    slot4 = random.choice(symbols)
    print_slots(slot1, slot2, slot3, slot4)
    
    if slot1 == slot2 == slot3 == slot4:
        winnings = bet * 50
        print(f"{Colors.GREEN}Congratulations, you hit the jackpot and won ${winnings}!{Colors.RESET}")
        balance += winnings
    elif slot1 == slot2 == slot3 or slot1 == slot2 == slot4 or slot1 == slot3 == slot4 or slot2 == slot3 == slot4:
        winnings = bet * 20
        print(f"{Colors.GREEN}Great! You hit three of a kind and won ${winnings}!{Colors.RESET}")
        balance += winnings
    elif (slot1 == slot2 and slot3 == slot4) or (slot1 == slot3 and slot2 == slot4) or (slot1 == slot4 and slot2 == slot3):
        winnings = bet * 10
        print(f"{Colors.YELLOW}Nice! You got two pairs and won ${winnings}!{Colors.RESET}")
        balance += winnings
    else:
        print(f"{Colors.RED}Sorry, better luck next time. You lost ${bet}.{Colors.RESET}")
        balance -= bet
    
    return balance

if __name__ == "__main__":
    balance = 100 
    balance = play_slots(balance)